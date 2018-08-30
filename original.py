#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import requests
import os
import speech_recognition as sr
from gtts import gTTS

def start():

	sample_rate = 48000
	chunk_size = 2048

	Count = 0
	SERVO=18
	status=3.5
	StepPins=[17,15,27,22]

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SERVO,GPIO.OUT)
	GPIO.output(SERVO, False)
	SERVO_PWM = GPIO.PWM(SERVO,50)
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


	while(1):
		r = sr.Recognizer()
		with sr.Microphone(device_index=2, sample_rate = sample_rate, chunk_size = chunk_size) as source:
			print("talk")
			audio1 = r.listen(source)
		try:
			voice1 = r.recognize_google(audio1, language='ko-KR')
			print(voice1)
		except sr.UnknownValueError:
			print("No!!")
			continue;
		except sr.RequestError as e:
			print(e)
		if(voice1!=u"헤이"):
			continue

		if(voice1==u"헤이"):
			with sr.Microphone(device_index=2, sample_rate = sample_rate, chunk_size = chunk_size) as source:
				os.system("mpg321 -o alsa medicine.mp3")
				audio = r.listen(source)
			try:
				voice = r.recognize_google(audio, language='ko-KR')
				print(voice)
			except sr.UnknownValueError:
				print("No!!")
			except sr.RequestError as e:
				print(e)


		if(voice.find( u"약 주세요")!=-1):
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
	# Wait	 before moving on
				Count += 1
				time.sleep(WaitTime)
				if (StepCounter==StepCount):
					StepCounter = 0
				if (StepCounter<0):
					StepCounter = StepCount
			Count=0
		elif(voice.find(u"물 주세요")!=-1):
		   print "water"
		   os.system("mpg321 -o alsa water.mp3")
		   print "11.5"
		   status=3.5
		   SERVO_PWM.ChangeDutyCycle(status)
		   time.sleep(3)
		   print "3.5"
		   status=11.5
		   SWERVO_PWM.ChangeDutyCycle(status)
		   time.sleep(2)

if __name__ == '__main__':
	start()
