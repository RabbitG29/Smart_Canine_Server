#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import requests
import os
import speech_recognition as sr
from gtts import gTTS

sample_rate = 48000
chunk_size = 2048

Count = 0

SWITCH=20
SWITCH2=16
SERVO=18
status=3.5
StepPins=[17,15,27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO,GPIO.OUT)
GPIO.output(SERVO, False)
SERVO_PWM = GPIO.PWM(SERVO, 50)
SERVO_PWM.start(0)
for pin in StepPins:
	print "Setup pins"
    	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)


StepCounter = 0
WaitTime = 0.001

StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

Seq = Seq2
StepCount = StepCount2

try:

	while (1):
		if GPIO.input(SWITCH2)==GPIO.HIGH:
			print "Switch2 Press"
			if (status==3.5):
				os.system("mpg321 -o alsa water.mp3")
				print "3.5"
				status=11.5
				SERVO_PWM.ChangeDutyCycle(status)
				time.sleep(2)
			elif (status==11.5):
				print "11.5"
				status=3.5
				SERVO_PWM.ChangeDutyCycle(status)
				time.sleep(2)

		if GPIO.input(SWITCH)==GPIO.HIGH:
			print('SWITCH is High. Pressed')
			os.system("mpg321 -o alsa medic.mp3")


			while Count<455:
				for pin in range(0, 4):
					xpin = StepPins[pin]
					if Seq2[StepCounter][pin]!=0:
						print " Step %i Enable %i" %(StepCounter,xpin)
						GPIO.output(xpin, True)
	    				else:
        					GPIO.output(xpin, False)
				StepCounter += 1
				 # If we reach the end of the sequence
					# start again
				if (StepCounter==StepCount):
  					StepCounter = 0
				if (StepCounter<0):
					StepCounter = StepCount
				  # Wait before moving on
				Count += 1
				time.sleep(WaitTime)
				if (StepCounter==StepCount):

					 StepCounter = 0

				if (StepCounter<0):

					 StepCounter = StepCount
			Count=0
#			r = requests.post("http://192.168.43.14:4000/", data={'test':'press'})
			print('Tongisin')
		else :
			print('SWITCH is Low')
		time.sleep(0.1)
				


except KeyboardInterrupt, e:
	pass
except Exception, e:
	print e
	pass
finally:
	GPIO.cleanup()


