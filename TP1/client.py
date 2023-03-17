import paho.mqtt.client as paho

# Set MQTT connection parameters
broker_address = "localhost"
port = 1883
username = "admin"
password = "admin"
topic = "Topic SSIE"

# Create MQTT client object
client = paho.Client()

# Set MQTT credentials
client.username_pw_set(username, password)

# Connect to MQTT broker and subscribe to topic
try:
    client.connect(broker_address, port=port)
    client.subscribe(topic)
except ConnectionRefusedError:
    print("Connection to MQTT broker failed. Please check if the broker is running.")

# Loop to listen for MQTT messages
client.loop_forever()
