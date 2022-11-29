# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )                              # Subscribe to all topics
 
def on_message(client, userdata, msg):                      # Func for receiving msgs
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
 
#def on_log(client, userdata, level, msg):
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

#dirpath = "/Users/kieranhulsman/Coding/SE-101/foralltimes/foralltimes" # kieran's local
dirpath = "/home/pi/Desktop/foralltimes/" # raspi

caPath = dirpath + "/aws-keys/AmazonRootCA1.pem"
certPath = dirpath + "/aws-keys/18e60f6a557bb07c315742faf1d00480e4fb3db3cf8d6b403a1dc3aaff799d41-certificate.pem.crt"
keyPath = dirpath + "/aws-keys/18e60f6a557bb07c315742faf1d00480e4fb3db3cf8d6b403a1dc3aaff799d41-private.pem.key"
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)      
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_forever()                                        # Start receiving in loop

