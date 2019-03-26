# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import serial
import time

app = Flask(__name__)

PORT_24D = "COM5"
PORT_BOGEL = "COM6"
BAUD_RATE = 9600
ON = 0
OFF = 1

# init usb relay
def initusb(deviceid):
   if(deviceid == "0"):
       fd=serial.Serial(PORT_24D,BAUD_RATE)
   elif(deviceid == "1"):
       fd=serial.Serial(PORT_BOGEL,BAUD_RATE)
   else:
       fd=serial.Serial(PORT_24D,BAUD_RATE)
   time.sleep(1)
   fd.write(str.encode('\x50'))
   time.sleep(0.5)
   fd.write(str.encode('\x51'))
   time.sleep(0.5)
   return fd

def open(deviceid,channel):
   fd = initusb(deviceid)
   cmd = '\x00'
   if(channel == "1"):
       cmd = '\x01'        
   elif(channel == "2"):
       cmd = '\x02'
   elif(channel == "3"):
       cmd = '\x04'
   elif(channel == "4"):
       cmd = '\x08'
   fd.write(str.encode(cmd))
   fd.close()
   print('Relay ' + channel + ' OPENED')
   return 'Relay ' + channel + ' OPENED'

def closeall(deviceid):
   fd = initusb(deviceid)
   cmd = '\x00'
   fd.write(str.encode(cmd))
   fd.close()
   print('All relay closed')
   return 'All relay closed'

@app.route('/suck_and_spin/<device_id>')
def suckandspin(device_id):
    try:
            print("request IP: ",request.remote_addr)        
            print("device_id : ", device_id)
            
            if(device_id == "0"): # 24D                                
                open(device_id,"2") #suck
                time.sleep(5)
                #
                closeall(device_id)
                time.sleep(2)
                #
                open(device_id,"3") #spin          
                time.sleep(2)
                #
                closeall(device_id)                
                time.sleep(1)
            elif(device_id == "1"): # Bogel                
                open(device_id,"2")
                time.sleep(10)
                #
                closeall(device_id)                
                time.sleep(1)            
    finally:  
            return 'SUCK AND SPIN FINISHED'

if __name__ == '__main__':
   app.run()