"""
I'm wrting the code here, but a copy of this will be in the dir ultrasonic, to be called by main.py
it was the easiest way to get the aws stuff working
- Kieran
"""
# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from time import sleep
from random import uniform
from datetime import datetime
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### AWS CERTIFICATION PATHS #### 
awshost = "a18avmdr8w67wa-ats.iot.us-east-2.amazonaws.com" # Endpoint
awsport = 8883 # Port no.   
clientId = "raspberry_pi" # Thing_Name
thingName = "raspberry_pi"

dirpath = "/Users/kieranhulsman/Coding/SE-101/SE101-project/foralltimes/aws" # kieran's local (testing)
#dirpath = "/home/pi/Desktop/foralltimes/aws" # raspi (actual)

caPath = dirpath + "/aws-keys/AmazonRootCA1.pem"
certPath = dirpath + "/aws-keys/18e60f6a557bb07c315742faf1d00480e4fb3db3cf8d6b403a1dc3aaff799d41-certificate.pem.crt"
keyPath = dirpath + "/aws-keys/18e60f6a557bb07c315742faf1d00480e4fb3db3cf8d6b403a1dc3aaff799d41-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None) # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60) # connect to aws server
 
mqttc.loop_start() # Start the loop

sleep(5)
if connflag == True:
    a = {
        "update": 1
    }

    x = json.dumps(a)
    mqttc.publish("foralltimes", x, qos=1)

'''
# testing
while 1==1:
    sleep(5)
    if connflag == True:
        
        msg = {
            "time": "{}".format(datetime.now()),
            "counter": "test passed"
        }
        a = {
            "update": 1
        }

        x = json.dumps(a)
        mqttc.publish("foralltimes", x, qos=1)
        
        #msg = json.dumps(msg)

        #mqttc.publish("foralltimes", msg , qos=1)       
        print("msg sent")
        print(x)

    else:
        print("waiting for connection...")
'''