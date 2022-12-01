# testing file
from aws_publish import *

while 1==1:
    sleep(5)
    if connflag == True:
        a = {
            "update": 1
        }
        x = json.dumps(a)
        mqttc.publish("foralltimes", x, qos=1)
        sleep(5)
        break