import os
import time
import sys
import json
import random
import paho.mqtt.client as mqtt

# Thingsboard platform credentials
THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN = 'LyoSMl8n9Yoki1fBpJoj'
request = {"method": "gettelemetry", "params": {}}

# MQTT on_connect callback function
def on_connect(client, userdata, flags, rc):
    print("rc code:", rc)
    client.subscribe('v1/devices/me/rpc/response/+')
    client.publish('v1/devices/me/rpc/request/1',json.dumps(request), 1)

# MQTT on_message caallback function
def on_message(client, userdata, msg):
    print('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))

# start the client instance
client = mqtt.Client()

# registering the callbacks
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883,60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    client.disconnect()
# https://demo.thingsboard.io/dashboard/50770330-7826-11ec-91d1-9b16bfb7b504?publicId=e1aef1d0-7823-11ec-91d1-9b16bfb7b504
