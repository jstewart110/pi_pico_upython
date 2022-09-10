
import time
import utime
from machine import Pin

TRIG = 27  #define the 16 ---input
ECHO = 26  #define the 18 ---input
trigger = Pin(TRIG, Pin.OUT)
echo = Pin(ECHO,Pin.OUT)


#notion BROAD
def setup():
    pass
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(TRIG, GPIO.OUT)
    #GPIO.setup(ECHO, GPIO.IN)

def distance():
    trigger.value(0)
    #GPIO.output(TRIG, 0)
    time.sleep_us(2)   #0.000002 s low

    trigger.value(1)
    #GPIO.output(TRIG, 1)
    time.sleep_us(1)  #0.000001 s high
    trigger.value(0)
    #GPIO.output(TRIG, 0)


    #while GPIO.input(ECHO) == 0:     #get the triger_begin
    while echo.value() == 0:
        a = 0
    time1 = utime.ticks_us()
    print(f'Time1:{time1}')
    while echo.value() == 1:
    #while GPIO.input(ECHO) == 1:     #get the triger_end
        a = 1
    time2 = time.ticks_us()   #voice begin-end time
    print(f'Time2:{time2}')
    print(f'TOF:{time2-time1}')
    
    during = utime.ticks_diff(time2, time1)
    return during * 314/1000 * 100 / 2.54 / 12 #* 340 / 2 * 10  #the speed of voice 314m/s

def loop():
    while True:
        #print('in loop')
        dis = distance()
        print(f'Distance: {dis:0.2f}')
        time.sleep(1)

def destroy():
    pass
    #GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
