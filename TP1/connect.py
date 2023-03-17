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

trames_envoyees = 0
# loop
for vehicule in data["véhicule"]:
    # send message
    client.publish(data["nom du topic MQTT"],genere_tram_1.generation_tram_1(vehicule))
    time.sleep(data["temps de latence"])
    trames_envoyees += 1
    if trames_envoyees >= data["nombre de trames"]:
        break

trames_envoyees = 0
for vehicule in data["véhicule"]:
    # send message
    client.publish(data["nom du topic MQTT"],genere_tram_2.generation_tram_2(vehicule))
    time.sleep(data["temps de latence"])
    trames_envoyees += 1
    if trames_envoyees >= data["nombre de trames"]:
        break
# disconnection
client.disconnect()