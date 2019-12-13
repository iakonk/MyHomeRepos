import sys
import select
import argparse
import zmq


class Client:

    def __init__(self, stop_on_loop):
        self.stop_on_loop = stop_on_loop # for integration tests
        self.context = zmq.Context()
        self.loops = 0

        self.sender_socket = self.context.socket(zmq.REQ)
        self.sender_socket.connect("tcp://127.0.0.1:8000")

        self.sub_socket = self.context.socket(zmq.SUB)
        self.sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
        self.sub_socket.connect("tcp://127.0.0.1:8001")

        # TBD: fix Only one client is able to send requests from one PC & all ops are blocking.
        # However, sub messages are queued, so client will receive them all
        self.stdin = select.select([sys.stdin], [], [], 10)[0]

    def send_message(self):
        if self.stdin:
            user_stdin = sys.stdin.readline().strip()
            print("Sending request: ", user_stdin, "...")
            self.sender_socket.send_string(user_stdin)
            reply = self.sender_socket.recv()
            print("Server replied: [", reply, "]")

    def poll_subscription(self):
        message = self.sub_socket.recv()
        print('Received server broadcast message: %s' % message)

    def close_all_sockets(self):
        self.sender_socket.close()
        self.sub_socket.close()

    def run_one_loop(self):
        self.loops += 1
        self.send_message()
        self.poll_subscription()

    def run(self):
        try:
            while True:
                self.run_one_loop()
                if self.stop_on_loop and self.stop_on_loop == self.loops:
                    self.close_all_sockets()
                    break
        except zmq.error.Again as exc:
            print(exc.strerror)
        finally:
            self.close_all_sockets()


def main(args):
    cli = Client(args.stop_on_loop)
    cli.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--stop-on-loop', default=None, type=int, required=False)
    args = parser.parse_args()
    try:
        main(args)
    except Exception as exc:
        raise exc
