from i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin, Timer
import utime

# Display stuff
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)
#i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Ultrasonic stuff
trigger1 = Pin(27, Pin.OUT)
echo1 = Pin(26, Pin.IN)
tim1 = Timer()
timepassed1=0

trigger2 = Pin(21, Pin.OUT)
echo2 = Pin(20, Pin.IN)
tim2 = Timer()
timepassed2=0

def ultra1(timer):
    global trigger1, echo1
    global timepassed1
    trigger1.low()
    utime.sleep_us(2)
    trigger1.high()
    utime.sleep_us(5)
    trigger1.low()
    while echo1.value() == 0:
        signaloff = utime.ticks_us()
    while echo1.value() == 1:
        signalon = utime.ticks_us()
    timepassed1 = signalon - signaloff

def ultra2(timer):
    global trigger2, echo2
    global timepassed2
    trigger2.low()
    utime.sleep_us(2)
    trigger2.high()
    utime.sleep_us(5)
    trigger2.low()
    while echo2.value() == 0:
        signaloff = utime.ticks_us()
    while echo2.value() == 1:
        signalon = utime.ticks_us()
    timepassed2 = signalon - signaloff


#initialize timer periodic callback for ultrasonic sensor
tim1.init(freq=2, mode=Timer.PERIODIC, callback=ultra1)
tim2.init(freq=2, mode=Timer.PERIODIC, callback=ultra2)

#print(i2c.scan())

# print out distance
#lcd.move_to(0,0)
#lcd.putstr('Distance: ')
while True:
    #for i in range(9,-1,-1):
    lcd.move_to(0,0)
    distance1 = (timepassed1 * 0.0343) / 2 / 2.54
    lcd.putstr(f'Dist1: {distance1:.1f}In  ')
    lcd.move_to(0,1)
    distance2 = (timepassed2 * 0.0343) / 2 / 2.54
    lcd.putstr(f'Dist2: {distance2:.1f}In  ')
    #lcd.putchar(str(i))
    #print(i)
    utime.sleep(1)
    