import json
import time
import random

# Opening the JSON file and handling potential errors
try:
    with open('data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: JSON file not found.")
    exit()

# Function to generate a message frame
def generate_message_1(vehicle):
    # Generating random data
    message = {'id': vehicle.get('VIN'), 'ts': round(time.time()), 'msg': random.choice([14, 56, 125])}

    if message['msg'] == 14:
        message.update({'lat': vehicle.get('lat'), 'long': vehicle.get('long'), 'r': vehicle.get('r')})
    
    if message['msg'] == 125:
        message.update({'pnb': vehicle.get('pnb')})
    
    if message['msg'] == 56:
        message.update({'a': vehicle.get('a'), 'v': vehicle.get('v'), 'c': vehicle.get('c')})

    # Creating a list of message attribute values
    values = [f"{key}={value}" for key, value in message.items()]

    # Concatenating the list into a string
    payload = ';'.join(values)

    # Handling errors for unknown messages
    if message['msg'] not in [14, 56, 125]:
        print(f"Error: Unknown message type: {message['msg']}")
        return None

    print(payload) # Displaying the message frame on the terminal
