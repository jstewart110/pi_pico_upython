import time, _thread, machine

# Define function with param 1 is number of times to loop and param2 is delay between off/on
def task(n, delay):
    led = machine.Pin(25, machine.Pin.OUT)
    for i in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
    print('done')

# Launch as a thread and return to REPL mode
_thread.start_new_thread(task, (10, 0.5))