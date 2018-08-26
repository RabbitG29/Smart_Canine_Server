#-*- coding: utf-8 -*-
from flask import Flask, request

from uuid import getnode as get_mac
from firebase import firebase
import datetime
import json
import time
from threading import *

app = Flask(__name__)
thread = None

# GET MAC ADDRESS

firebase = firebase.FirebaseApplication('https://smartcanine-c15e7.firebaseio.com/',None)


def getMac():
    mac = get_mac()
    char_mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    return char_mac
def deviceInit(mac):
    print('Start Init Data for' + mac)
    result = firebase.get('/devices', None, params={'shallow': 'true'})
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
    print(firebase.put('/devices/'+mac, 'status', dat))
    json_data = open('canine_config.json').read()
    data = json.loads(json_data)
    serial = data['serialNo']
    print(firebase.put('/devices/'+mac, 'serialNumber', serial))
    print(firebase.patch('/devices/'+mac, {'currentPos':'0'}))

def insertPill(name, quantity, slot, dosetime):
    # CONNECT TO FIREBASE
    result = firebase.get('/devices', None, params={'shallow': 'true'})

def StabStatus():
    print('Running Scheduled Task : ')
    # CONNECT TO FIREBASE
    result = firebase.get('/devices', None, params={'shallow': 'true'})

    # CHECK DOES MAC ADDRESS ALREADY EXIST
    mac = getMac()
    if result==None:
        r = firebase.patch('/devices/'+mac, {'timestamp': str(datetime.datetime.now())})        
        print(r)
        deviceInit(mac)

    elif result.get(mac, None)==None:
        r = firebase.put('/devices', mac, {'timestamp': str(datetime.datetime.now())})
        print(r)
        deviceInit(mac)
        
    else : 
        r = firebase.patch('/devices/'+mac, {'timestamp': str(datetime.datetime.now())})
        print(r)


@app.route("/", methods = ['POST'])
def backgound_thread():
    if request.method == 'POST':
	print("Hi")
        user = request.form['test']
        print(user)
	result = firebase.get('/devices/0A:00:27:00:00:17/currentPos', None, params={'shallow': 'true'})
	result2 = int(result);
	result2+=1;
	if(result2==9):
		result2=0;
	print(str(result2))
        firebase.patch('/devices/0A:00:27:00:00:17/', {'currentPos': result2})

	return "Hello"
def start():
	app.run(host='localhost', port=4000, debug=True)
if __name__ == "__main__":
	start()
