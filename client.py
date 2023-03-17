import paho.mqtt.client as paho

# Configuration des paramètres de connexion MQTT
broker_address = "localhost"
port = 1883
username = "admin"
password = "admin"

# Définition de la fonction de rappel pour les messages MQTT
def on_message(client, userdata, message):
    print("Message reçu : " + str(message.payload.decode("utf-8")))

# Création d'un client MQTT
client = paho.Client()

# Configuration des identifiants de connexion MQTT
client.username_pw_set(username, password)

# Configuration de la fonction de rappel pour les messages MQTT
client.on_message = on_message

# Connexion au broker MQTT et souscription aux sujets
client.connect(broker_address, port=port)
client.subscribe("topic/Topic SSIE")

# Boucle d'écoute des messages MQTT en permanence
client.loop_forever()
