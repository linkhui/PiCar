#coding=utf-8
import RPi.GPIO as GPIO
import time

import distance
    
#定义信号接口gpio口,后面的数字是对应的BCM模式的GPIO编号
INT1 = 12 #18
INT2 = 13 #27
INT3 = 15 #22
INT4 = 16 #23
 
def init():
    GPIO.setmode(GPIO.BOARD)


    #GPIO.cleanup()

    GPIO.setup(INT1,GPIO.OUT)
    GPIO.setup(INT2,GPIO.OUT)
    GPIO.setup(INT3,GPIO.OUT)
    GPIO.setup(INT4,GPIO.OUT)
    
    distance.initDistanceGPIO()

def back(sleep_time):
    GPIO.output(INT1, True)
    GPIO.output(INT2, False)
    GPIO.output(INT3, True)
    GPIO.output(INT4, False)
    time.sleep(sleep_time)

def forward(sleep_time):
    GPIO.output(INT1, False)
    GPIO.output(INT2, True)
    GPIO.output(INT3, False)
    GPIO.output(INT4, True)
    time.sleep(sleep_time)

#左转
def left(sleep_time):
    GPIO.output(INT1,False)
    GPIO.output(INT2,False)
    GPIO.output(INT3,True)
    GPIO.output(INT4,False)
    time.sleep(sleep_time)

#右转
def right(sleep_time):
    GPIO.output(INT1,True)
    GPIO.output(INT2,False)
    GPIO.output(INT3,False)
    GPIO.output(INT4,False)
    time.sleep(sleep_time)

def stop(sleep_time):
    GPIO.output(INT1, False)
    GPIO.output(INT2, False)
    GPIO.output(INT3, False)
    GPIO.output(INT4, False)

if __name__ == "__main__":
    init()
    
    distance.checkdist()

    back(5)

    stop(2)

    forward(5)

    GPIO.cleanup()

    
    
