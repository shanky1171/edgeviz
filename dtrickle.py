#!/usr/bin/python

import sys, getopt
from datetime import datetime
from datetime import timedelta
from random import seed
from random import randint 
import json
import time 
import requests

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

def main(argv):
    # Arguments passed
    print("\nName of Python script:", sys.argv[0])
    print("\nValue for iteration  :", sys.argv[1])
    print("\nTime Interval        :", sys.argv[2])

    for i in range(int(sys.argv[1])):
        for j in range(1,6):
            tstamp = datetime.now()
            temp = randint(30, 40)
            humidity = randint(50, 80)
            pressure = randint(90, 120)
            dev=1
            rec = {
	        "pressure":pressure,
	        "humidity":humidity,
	        "temp":temp,
	        "ts": tstamp,
	        "deviceId": j
            }
            #print(rec) 
            jtsdata = json.dumps(rec, default = myconverter)
            print(jtsdata)
            url='http://localhost/tsdataput'
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(url, data=jtsdata, headers=headers)
            print(r.text)
        time.sleep(int(sys.argv[2]))

if __name__ == "__main__":
   main(sys.argv[1:])
