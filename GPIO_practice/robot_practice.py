import RPi.GPIO as GPIO
import time

#Set GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

#Set up i/o pins for front wheels
#Front Left
GPIO.setup(7,GPIO.OUT)
#Front Right
GPIO.setup(13,GPIO.OUT)


#i/o pins for the rear wheels
#Rear left
GPIO.setup(11,GPIo.OUT)
#Rear Right
GPIO.setup(15,GPIO.OUT)

#Test each motor:
GPIO.output(7,True)
time.sleep(1)

GPIO.output(7,False)
GPIO.output(13,True)
time.sleep(1)

GPIO.output(13,False)
GPIO.output(11,True)
time.sleep(1)

GPIO.output(11,False)
GPIO.output(13,True)
time.sleep(1)

GPIO.output(13,False)
GPIO.output(15,True)
time.sleep(1)

GPIO(15,False)
GPIO.cleanup()
