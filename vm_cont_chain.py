#!/bin/bash

# Replace these variables with your actual broker address and username
BROKER_ADDRESS="172.20.10.4"
USERNAME="VLAWTON"

# Subscribe to the ping topic and process incoming messages
mosquitto_sub -h "$BROKER_ADDRESS" -t "$USERNAME/ping" | while read -r MSG
do
  # Increment the received number
  NEW_NUMBER=$((MSG + 1))

  # Publish the incremented number to the pong topic
  mosquitto_pub -h "$BROKER_ADDRESS" -t "$USERNAME/pong" -m "$NEW_NUMBER"
done
