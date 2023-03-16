import json
import time
import random

# Ouverture du fichier JSON
with open('data.json') as f:
    data = json.load(f)

def generation_tram_1(vehicule):
    # Génération des données aléatoires
    msg = {}
    msg['id'] = vehicule['VIN']

    # Récupérer le timestamp
    timestamp = round(time.time())
    msg['ts'] = timestamp
    msg['msg'] = random.choice([14, 56, 125])
    payload = 'id={};msg={};ts={}'.format(msg['id'], msg['msg'], msg['ts'])

    if msg['msg'] == 14:
        msg['lat'] = vehicule['lat']
        msg['long'] = vehicule['long']
        msg['r'] = vehicule['r']
        payload += ';lat={}'.format(msg['lat']) + ';long={}'.format(msg['long']) + ';r={};'.format(msg['r'])
    
    if msg['msg'] == 125:
        msg['pnb'] = vehicule['pnb']
        payload += ';pnb={};'.format(msg['pnb'])
    
    if msg['msg'] == 56:
        msg['a'] = vehicule['a']
        msg['v'] = vehicule['v']
        msg['c'] = vehicule['c']
        payload += ';a={}'.format(msg['a']) + ';v={}'.format(msg['v']) + ';c={};'.format(msg['c'])

    print(payload) # Affichage de la trame sur le terminal

