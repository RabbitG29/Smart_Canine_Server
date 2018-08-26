
import main
import switch
import voice
import firecron

from time import sleep

from multiprocessing import Process

process = []
pid = []
pname = ['flask', 'switch', 'voice', 'firecron']
target = [main.start, switch.start, voice.start, firecron.start]

def monitor():
    while True:
#        print(target)
        if len(process) > 0:
            for i in range(len(process)):
                if process[i].is_alive():
                    print(pname[i]+'('+str(pid[i])+') is on')
                else:
                    print(pname[i]+'('+str(pid[i])+') is off')

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


