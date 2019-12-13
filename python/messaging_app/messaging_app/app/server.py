import os
import signal
import functools
import argparse
import asyncio
import zmq

from zmq.asyncio import Context


class Server:

    def __init__(self, stop_on_loop):
        self.stop_on_loop = stop_on_loop  # for integration tests
        self.messages_queue = asyncio.Queue()
        self.context = Context()
        self.sleep_sec = 1
        self.loops = 0

        self.receiver_socket = self.context.socket(zmq.REP)
        self.receiver_socket.bind("tcp://127.0.0.1:8000")

        self.pub_socket = self.context.socket(zmq.PUB)
        self.pub_socket.bind("tcp://*:8001")

    async def receive_message(self):
        received_message = await self.receiver_socket.recv()
        self.messages_queue.put_nowait(received_message)
        await asyncio.sleep(self.sleep_sec)
        await self.receiver_socket.send_string("Echo reply from the server: %s" % received_message)

    async def publish_message(self):
        message_to_publish = await self.messages_queue.get()
        await self.pub_socket.send(message_to_publish)
        self.messages_queue.task_done()
        await asyncio.sleep(self.sleep_sec)

    async def wait_until_all_messages_published(self):
        await self.messages_queue.join()

    async def run_one_loop(self):
        self.loops += 1
        await asyncio.gather(
            self.receive_message(),
            self.publish_message(),
            self.wait_until_all_messages_published(),
            return_exceptions=True
        )

    async def run(self):
        while True:
            await self.run_one_loop()
            print('running server loop #no: ', self.loops)
            if self.stop_on_loop and self.stop_on_loop == self.loops:
                self.receiver_socket.close()
                self.pub_socket.close()
                break


def main(loop, args):
    server = Server(args.stop_on_loop)
    loop.run_until_complete(server.run())


def signal_handler(sig, loop):
    loop.remove_signal_handler(sig)
    os.killpg(0, sig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--stop-on-loop', default=None, type=int, required=False)
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    for signame in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(signame, functools.partial(signal_handler, signame, loop))

    try:
        main(loop, args)
    except Exception as exc:
        raise exc
    finally:
        loop.close()
        if not args.stop_on_loop:
            os.killpg(0, signal.SIGTERM)
