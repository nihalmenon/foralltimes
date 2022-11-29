# testing file
from aws_publish import *

a = {
    "time": "{}".format(datetime.now()),
    "msg": "me please lemme write it",
}

x = json.dumps(a)
mqttc.publish("foralltimes", x, qos=1)