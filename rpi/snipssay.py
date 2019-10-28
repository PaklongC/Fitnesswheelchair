from hermes_python.hermes import Hermes, MqttOptions

def snips_say(message):
    with Hermes(mqtt_options=MqttOptions()) as h:
    	h.publish_start_session_notification(None,message,None)
