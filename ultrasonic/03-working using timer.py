from machine import Pin, Timer
import utime

trigger = Pin(27, Pin.OUT)
echo = Pin(26, Pin.IN)
tim = Timer()
timepassed=0

def ultra(timer):
    global trigger, echo
    global timepassed
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff

#if __name__ == "__main__":
tim.init(freq=2, mode=Timer.PERIODIC, callback=ultra)
#setup()
try:
    while True:
        #ultra()
        distance = (timepassed * 0.0343) / 2 / 2.54
        print(f"The distance from object is {distance:3.1f} inches")
        utime.sleep(1)
except KeyboardInterrupt:
    tim.deinit()

