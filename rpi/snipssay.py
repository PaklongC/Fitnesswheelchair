from hermes_python.hermes import Hermes, MqttOptions
#simple TTS script that sends a string over mqqt localhost:1883.
#The snips platform is listening to this and when the adress (first None) is not specified it will use snips TTS say
#for more information see https://docs.snips.ai/reference/dialogue
#And https://hermespython.readthedocs.io/en/latest/tutorial.html
def snips_say(message):
    with Hermes(mqtt_options=MqttOptions()) as h:
    	h.publish_start_session_notification(None,message,None)
        print("Snips TTS:",message)
#snips say but with an variable as second argument
def snips_sayx(message,x):
    with Hermes(mqtt_options=MqttOptions()) as h2:
        message += str(x)
        h2.publish_start_session_notification(None,message,None)
