from machine import Pin
import utime
trigger = Pin(27, Pin.OUT)
echo = Pin(26, Pin.IN)
def ultra():
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
   distance = (timepassed * 0.0343) / 2 / 2.54
   print(f"The distance from object is {distance:3.1f} inches")
while True:
   ultra()
   utime.sleep(1)