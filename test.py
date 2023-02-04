import time
import continuous_threading


counter = [0]

def inc_counter():
    counter[0] += 1

th = continuous_threading.PausableThread(target=inc_counter)

th.start()
time.sleep(4)

th.stop()
time.sleep(4)

value = counter[0]
assert value > 0

time.sleep(0.1)
assert value == counter[0]

th.start()
time.sleep(0.1)
