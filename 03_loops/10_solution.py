import time

wait_time = 1  #time in second (1 sec given)
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1