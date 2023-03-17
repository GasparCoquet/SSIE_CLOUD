import json
import time

# Ouverture du fichier JSON
with open('data.json') as f:
    data = json.load(f)

def generation_tram_2(vehicule):
    # Génération des données aléatoires
    msg = {}
    msg['id'] = vehicule['VIN']
    # Récupérer le timestamp
    timestamp = round(time.time())
    msg['ts'] = timestamp
    msg['lat'] = vehicule['lat']
    msg['long'] = vehicule['long']
    msg['a'] = vehicule['a']
    msg['pnb'] = vehicule['pnb']
    msg['c'] = vehicule['c']
    msg['v'] = vehicule['v']
    payload = '{}|{}|{}|{}|{}|{}|{}|{}'.format(msg['id'], msg['lat'], msg['long'], msg['a'], msg['ts'], msg['pnb'], msg['c'], msg['v'])
    print(payload) # Affichage de la trame sur le terminal

