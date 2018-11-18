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
GPIO.setup(11,GPIO.OUT)
#Rear Right
GPIO.setup(15,GPIO.OUT)

'''
#Test each motor:
GPIO.output(7,True)
print('Front left motor active')
time.sleep(1)

GPIO.output(7,False)
print('Front left motor deactivated')
GPIO.output(13,True)
print('Front right motor active')
time.sleep(1)

GPIO.output(13,False)
print('Front right motor deactivated')
GPIO.output(11,True)
print('Rear Left motor active')
time.sleep(1)

GPIO.output(11,False)
print('Rear left motor deactivated')
GPIO.output(15,True)
print('Rear right motor active')
time.sleep(1)

GPIO.output(15,False)
print('Rear right motor deactivated')
time.sleep(1)

GPIO.output(15,False)
GPIO.cleanup()

'''
#Test forward, pause, reverse
GPIO.output(7,True)
GPIO.output(13,True)
time.sleep(2)

GPIO.output(7,False)
GPIO.output(13,False)
time.sleep(1)

GPIO.output(11,True)
GPIO.output(15,True)
time.sleep(2)

GPIO.output(11,False)
GPIO.output(15,False)

GPIO.cleanup()