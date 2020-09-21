import time
import subprocess as sp

from unittest.mock import Mock


def send_email(hostname, prev_state, curr_state):
    msg = 'Host: %s, state changed from %s to %s' % (hostname, prev_state, curr_state)
    print(msg)


def run_one_loop(hostname):
    state = set()
    cnt = 2
    while cnt >= 0:
        exit_code = sp.check_call(['ping', hostname])
        curr_state = "DOWN" if exit_code else "UP"
        state.add(curr_state)
        cnt -= 1
        time.sleep(1)
    return state.pop() if len(state) == 1 else None


def run_loops(hostname, stop_on_loop=None):
    loops = 0
    prev_state = "DOWN"
    while True:
        curr_state = run_one_loop(hostname)
        if curr_state and curr_state != prev_state:
            send_email(hostname, prev_state, curr_state)
            prev_state = curr_state
        loops += 1
        if stop_on_loop and stop_on_loop == loops:
            break


# check that run_one_loop returns expected result
time = Mock()
state = {1: "DOWN", 0: "UP"}
for one_code in state:
    sp = Mock()
    sp.check_call.return_value = one_code
    res = run_one_loop('localhost')
    assert res == state[one_code]
    assert sp.check_call.call_count == 3

# test that email is sent when status changes
run_one_loop = Mock(return_value="UP")
send_email = Mock()
run_loops('localhost', stop_on_loop=1)
send_email.assert_called_with("localhost", "DOWN", "UP")

# test that email is not sent when status is None or remains the same
for state in ("DOWN", None):
    run_one_loop = Mock(return_value=state)
    send_email = Mock()
    run_loops('localhost', stop_on_loop=1)
    send_email.assert_not_called()
