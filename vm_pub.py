""" 
Victoria Lawton
Sriya Kuruppath
https://github.com/victorialawton/ee250lab4.git
"""

"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

# This function (or "callback") will be executed when this client receives 
# a connection acknowledgement packet response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code " + str(rc))

if __name__ == '__main__':
    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # Create a client object
    client = mqtt.Client()
    
    # Attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    # Connect to the MQTT broker
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    
    # Start the loop
    client.loop_start()
    time.sleep(1)

    while True:
        # Publish IP address
        client.publish("user/ipinfo", f"IP Address: {ip_address}")
        print("Publishing IP Address")

        # Get date and time
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        # Publish date and time in their own topics
        client.publish("user/date", f"Date: {date_str}")
        print("Publishing Date:", date_str)

        client.publish("user/time", f"Time: {time_str}")
        print("Publishing Time:", time_str)

        time.sleep(4)  # Wait for 4 seconds before next publish

