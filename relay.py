# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:37:13 2019

@author: rp
"""
import serial
import time

PORT = "COM5"
BAUD_RATE = 9600
ON = 0
OFF = 1

fd=serial.Serial(PORT,BAUD_RATE)
time.sleep(1)
fd.write(str.encode('\x50'))
time.sleep(0.5)
fd.write(str.encode('\x51'))
time.sleep(0.5)


def startAll():
    print("all-on")
    fd.write(str.encode('\xff'))
    
def stopAll():
    print("all-off")
    fd.write(str.encode('\x00'))

def relay1(onoff):
    if(onoff == "ON"): 
        cmd = '\x01'
    else:
        cmd = '\x11'
    fd.write(str.encode(cmd))

def relay2(onoff):
    if(onoff == "ON"): 
        cmd = '\x02'
    else:
        cmd = '00000000'
    fd.write(str.encode(cmd))


stopAll()
time.sleep(5)
#relay1("ON")
#print("relay 1 ON")
#time.sleep(5)
#
#relay2("ON")
#print("relay 2 ON")
#time.sleep(5)
#fd.write(str.encode('\x01'))  # relay 1 on
#fd.write(str.encode('\x02'))  # relay 2 on
fd.write(str.encode('\x04'))  # relay 3 on
#fd.write(str.encode('\x08'))  # relay 4 on

time.sleep(5)
#relay1("OFF")
stopAll()

#for x in range(0,4):
#    startAll()
#    time.sleep(5)
#    stopAll()
#    time.sleep(5)

time.sleep(1)
fd.close()
    