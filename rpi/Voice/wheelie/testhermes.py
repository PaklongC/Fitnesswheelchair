from hermes_python.hermes import Hermes, MqttOptions

MQTT_ADDR = " localhost:1883" 
with Hermes(mqtt_options=MqttOptions()) as h:
	h.publish_start_session_notification(None,"Super hacker pro",None) 
