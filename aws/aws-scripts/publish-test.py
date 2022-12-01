# testing file
from aws_publish import *

a = {
    "counter": 1
}

x = json.dumps(a)
mqttc.publish("foralltimes", x, qos=1)