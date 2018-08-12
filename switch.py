import RPi.GPIO as GPIO
import time
import requests
SERVO=16
SWITCH=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO,GPIO.OUT)
SERVO_PWM=GPIO.PWM(SERVO,50)
SERVO_PWM.start(0)
try:

	while (1):
		if GPIO.input(SWITCH)==GPIO.HIGH:
			print('SWITCH is High. Pressed')
			r = requests.post("http://192.168.43.14:4000/", data={'test':'press'})
			
			print('Tongisin')
			SERVO_PWM.ChangeDutyCycle(1)
			time.sleep(1)
			SERVO_PWM.ChangeDutyCycle(10)
			time.sleep(0.1)
		else :
			print('SWITCH is Low')
		time.sleep(0.1)

except KeyboardInterrupt, e:
	pass
except Exception, e:
	pass
finally:
	GPIO.cleanup()


