import json
import time

# Opening the JSON file and handling potential errors
try:
    with open('data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: JSON file not found.")
    exit()

def generate_message_2(vehicle):
    # Generating random data
    message = {
        'id': vehicle.get('VIN'),
        'ts': round(time.time()),
        'lat': vehicle.get('lat'),
        'long': vehicle.get('long'),
        'a': vehicle.get('a'),
        'pnb': vehicle.get('pnb'),
        'c': vehicle.get('c'),
        'v': vehicle.get('v')
    }

    # Handling errors for missing vehicle attributes
    for key, value in message.items():
        if value is None:
            print(f"Error: Missing vehicle attribute: {key}")
            return None

    # Creating a string with message attributes separated by pipes
    payload = '{}|{}|{}|{}|{}|{}|{}|{}'.format(
        message['id'], message['lat'], message['long'], message['a'], message['ts'], message['pnb'], message['c'], message['v']
    )
    print(payload) # Displaying the message frame on the terminal
