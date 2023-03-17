import paho.mqtt.client as paho
import time
import json
from generate_message_1 import generate_message_1
from generate_message_2 import generate_message_2

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Create MQTT client object
client = paho.Client("example")

# Connect to MQTT broker
try:
    client.connect("localhost", 1883)
except ConnectionRefusedError:
    print("Connection to MQTT broker failed. Please check if the broker is running.")

# Initialization of messages counter
frames_send = 0

# Send messages for vehicle data
for vehicule in data["vehicle"]:
    # Send message using generate_message_1
    client.publish(data["Name of MQTT Topic"], generate_message_1(vehicule))
    time.sleep(data["latency"])

    # Increment sent messages counter
    frames_send += 1

    # Stop sending messages if the specified number of frames has been reached
    if frames_send >= data["number of frames"]:
        break

# Reset sent messages counter
frames_send = 0

# Send messages for another type of vehicle data
for vehicule in data["vehicle"]:
    # Send message using generate_message_2
    client.publish(data["Name of MQTT Topic"], generate_message_2(vehicule))
    time.sleep(data["latency"])

    # Increment sent messages counter
    frames_send += 1

    # Stop sending messages if the specified number of frames has been reached
    if frames_send >= data["number of frames"]:
        break

# Disconnect from MQTT broker
client.disconnect()