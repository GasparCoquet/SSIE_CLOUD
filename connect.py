import paho.mqtt.client as paho
import time
import json
import genere_tram_1
import genere_tram_2

# Ouverture du fichier JSON
with open('data.json') as f:
    data = json.load(f)

# create client object
client = paho.Client("example")
# establish connection
client.connect("localhost", 1883)

i = 0
# loop
for vehicule in data["véhicule"]:
    # send message
    client.publish(data["nom du topic MQTT"], "val_" + str(i+1))
    genere_tram_1.generation_tram_1(vehicule)
    time.sleep(data["temps de latence"])
for vehicule in data["véhicule"]:
    # send message
    client.publish(data["nom du topic MQTT"], "val_" + str(i+1))
    genere_tram_2.generation_tram_2(vehicule)
    time.sleep(data["temps de latence"])
# disconnection
client.disconnect()