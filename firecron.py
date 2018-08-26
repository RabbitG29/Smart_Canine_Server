from uuid import getnode as get_mac
from firebase import firebase
import datetime
import json
import time
from threading import *
# GET MAC ADDRESS
def getMac():
    mac = get_mac()
    char_mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    return char_mac
def deviceInit(mac):
    print('Start Init Data for' + mac)
    f= firebase.FirebaseApplication('https://smartcanine-c15e7.firebaseio.com/')
    result = f.get('/devices', None, params={'shallow': 'true'})
    dat = {
        "0": {'content': '', 'dosetime': ''},
        "1": {'content': '', 'dosetime': ''},
        "2": {'content': '', 'dosetime': ''},
        "3": {'content': '', 'dosetime': ''},
        "4": {'content': '', 'dosetime': ''},
        "5": {'content': '', 'dosetime': ''},
        "6": {'content': '', 'dosetime': ''},
        "7": {'content': '', 'dosetime': ''},
        "8": {'content': '', 'dosetime': ''}
    }
    print(f.put('/devices/'+mac, 'status', dat))
    json_data = open('canine_config.json').read()
    data = json.loads(json_data)
    serial = data['serialNo']
    print(f.put('/devices/'+mac, 'serialNumber', serial))
    print(f.patch('/devices/'+mac, {'currentPos':'0'}))

def insertPill(name, quantity, slot, dosetime):
    # CONNECT TO FIREBASE
    f= firebase.FirebaseApplication('https://smartcanine-c15e7.firebaseio.com/')
    result = f.get('/devices', None, params={'shallow': 'true'})

def StabStatus():
    # CONNECT TO FIREBASE
    f= firebase.FirebaseApplication('https://smartcanine-c15e7.firebaseio.com/')
    result = f.get('/devices', None, params={'shallow': 'true'})

    # CHECK DOES MAC ADDRESS ALREADY EXIST
    mac = getMac()
    if result==None:
        r = f.patch('/devices/'+mac, {'timestamp': str(datetime.datetime.now())})
        deviceInit(mac)
        print(r)
    elif result.get(mac, None)==None:
        r = f.put('/devices', mac, {'timestamp': str(datetime.datetime.now())})
        deviceInit(mac)
        print(r)
    else : 
        r = f.patch('/devices/'+mac, {'timestamp': str(datetime.datetime.now())})
        print(r)

def cron():
    while(True):
        StabStatus()
        time.sleep(5)
def start():
    t = Timer(5.0, cron)
    t.start()

if __name__ == '__main__':
    start()