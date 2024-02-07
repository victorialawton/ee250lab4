""" 
Victoria Lawton
Sriya Kuruppath
https://github.com/victorialawton/ee250lab4.git
"""

"""EE 250L Lab 04 Starter Code
Run vm_pub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt

# This function will be executed when the client receives a connection acknowledgement packet response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code " + str(rc))
    
    # Subscribe to the topics of interest
    client.subscribe("user/ipinfo")
    client.subscribe("user/date")
    client.subscribe("user/time")
    
    # Add custom callbacks for specific topics
    client.message_callback_add("user/ipinfo", on_message_from_ipinfo)
    client.message_callback_add("user/date", on_message_from_date)
    client.message_callback_add("user/time", on_message_from_time)

# Default callback for messages
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload.decode()))

# Custom callback for IP information
def on_message_from_ipinfo(client, userdata, message):
    print("IP Address: " + message.payload.decode())

# Custom callback for Date
def on_message_from_date(client, userdata, message):
    print("Current Date: " + message.payload.decode())

# Custom callback for Time
def on_message_from_time(client, userdata, message):
    print("Current Time: " + message.payload.decode())

if __name__ == '__main__':
    # Create a client object
    client = mqtt.Client()

    # Attach a default callback for incoming MQTT messages
    client.on_message = on_message

    # Attach the on_connect() callback function
    client.on_connect = on_connect
    
    # Connect to the MQTT broker
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

    # Start the loop
    client.loop_forever()

