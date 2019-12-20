#!/usr/bin/env python
#coding=utf-8

from sense_hat import SenseHat

sense = SenseHat()

import logging

logging.basicConfig(filename='/home/pi/presence/presence-detector.log',level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Starting presence detector')

import subprocess

from time import sleep

#Names of device owners
names = ["Micks","Someone Else"]

# MAC addresses of devices
macs = ["74:da:38:fc:eb:96","xx:xx:xx:xx:xx:xx"]

def arp_scan():
        try:
                output = subprocess.check_output("sudo arp-scan -l", shell=True)
                for i in range(len(names)):
                        result = names[i]
                        if macs[i] in output:
                                result=result+" is home"
                        else:
                                result=result+" is not home"
                        print(result)
                        sense.show_message(result)
        except Exception as e:
                logging.error(e)

while True:
        arp_scan()
        sleep(30)
