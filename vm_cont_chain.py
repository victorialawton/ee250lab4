import paho.mqtt.client as mqtt
import time

# Replace these with your actual username and broker address
YOUR_USERNAME = "VLAWTON"
BROKER_ADDRESS = "172.20.10.4"

# Callback when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(f"{YOUR_USERNAME}/ping")

# Callback when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    number = int(msg.payload) + 1
    print(f"Received ping: {number}")
    time.sleep(1)
    client.publish(f"{YOUR_USERNAME}/pong", str(number))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks, and handles reconnecting.
client.loop_forever()

