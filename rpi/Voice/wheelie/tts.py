import paho.mqtt.client as mqtt #import the client1
broker_address="145.94.230.216"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("SnipsTTS") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("hermes/tts/say")
client.publish("hermes/tts/say","{\"text\": \"Super hacker jwz\"}")
