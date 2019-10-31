from hermes_python.hermes import Hermes, MqttOptions

def snips_say(message):
    with Hermes(mqtt_options=MqttOptions()) as h:
    	h.publish_start_session_notification(None,message,None)
def snips_sayx(message,x):
    with Hermes(mqtt_options=MqttOptions()) as h2:
        message += str(x)
        h2.publish_start_session_notification(None,message,None)
