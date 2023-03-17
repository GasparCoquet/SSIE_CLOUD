import paho.mqtt.client as paho

# Configuration des paramètres de connexion MQTT
broker_address = "localhost"
port = 1883
username = "admin"
password = "admin"

# Création d'un client MQTT
client = paho.Client()

# Configuration des identifiants de connexion MQTT
client.username_pw_set(username, password)

# Connexion au broker MQTT et souscription aux sujets
client.connect(broker_address, port=port)
client.subscribe("Topic SSIE")

# Boucle d'écoute des messages MQTT en permanence
client.loop_forever()
