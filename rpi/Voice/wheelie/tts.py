import paho.mqtt.client as mqtt #import the client1
broker_address="localhost:1883"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("SnipsTTS") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("hermes/tts/say")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("hermes/tts/say","Super hacker jwz")
