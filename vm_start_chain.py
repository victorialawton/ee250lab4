import paho.mqtt.client as mqtt
import time

# Replace these with your actual username and broker address
YOUR_USERNAME = "VLAWTON"
BROKER_ADDRESS = "172.20.10.4"

# Initial number to start the ping-pong chain
number = 0

# Callback when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(f"{YOUR_USERNAME}/pong")

# Callback when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global number
    number = int(msg.payload) + 1
    print(f"Received pong: {number}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, 1883, 60)

# Start a loop to keep the script running and listening for messages
client.loop_start()

while True:
    time.sleep(1)
    print(f"Sending ping: {number}")
    number += 1
    client.publish(f"{YOUR_USERNAME}/ping", str(number))






