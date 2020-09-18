import time
import subprocess as sp

HOSTNAME = 's'


def send_email():
    pass


def run_one_loop():
    state = set()
    cnt = 2
    while cnt >= 0:
        exit_code = sp.check_call(['ping', HOSTNAME])
        if exit_code:
            state.add("DOWN")
        else:
            state.add("UP")
        cnt -= 1
        time.sleep(1)
    return state[0] if state[0] == state[1] else None


last_state = "DOWN"
while True:
    curr_state = run_one_loop()
    if curr_state and curr_state != last_state:
        last_state = curr_state
        send_email()
