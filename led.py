
import main
import switch
import voice
import firecron

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


from time import sleep

from multiprocessing import Process

process = []
pid = []
pname = ['flask', 'switch', 'voice', 'firecron']
target = [main.start, switch.start, voice.start, firecron.start]
pled = [10, 9, 11, 0]
for l in pled:
    GPIO.setup(l, GPIO.OUT)
def monitor():
    while True:
        if len(process) > 0:
            for i in range(len(process)):
                if process[i].is_alive():
                    print(pname[i]+'('+str(pid[i])+') is on')
		    GPIO.output(pled[i], GPIO.HIGH)
                else:
                    print(pname[i]+'('+str(pid[i])+') is off')
		    GPIO.output(pled[i], GPIO.LOW)



        sleep(1)

if __name__ == '__main__':
    pm = Process(target = monitor)
    for _p in target:
        p = Process(target = _p)
        p.daemon = True
        p.start()
        pid.append(p.pid)
        process.append(p)
    monitor()


