from snipssay import snips_say, snips_sayx
from time import time
from random import randrange

global target_distance,target_velocity,velocity_min,velocity_max
#set default variables
distance=0
target_distance=1000
velocity=0
target_velocity= 200
deviation_velocity=20
velocity_min = target_velocity - deviation_velocity
velocity_max = target_velocity + deviation_velocity
start_time = time()
ltime_update = time()
ltime_positive = time()
ltime_slow = time() + 10
#array with voice lines that snips uses when you are too slow
lines_slow = ["Push a bit harder, you can do it","try going faster", "You are a bit to slow", "go faster", "go go go","Atleast you are not standing still but try harder","are you even moving","are you even trying","I dont think you are trying","you are not a good roll model"]
timeout_update=60
timeout_slow=20
#try:

#Get the config from the config.txt
#read config.txt
with open("config.txt","r") as properties:
    global d
    #convert to a list
    l = [line.split("=") for line in properties.readlines()]
    #convert to a python dictionary
    d = {key.strip(): value.strip() for key, value in l}
    #set our variables according to the dictionary we got from config.txt
    target_distance = int(d['target_distance'])
    target_velocity = int(d['target_velocity'])
    timeout_slow = int(d['timeout_slow'])
    timeout_update= int(d['timeout_update'])
    deviation_velocity = float(p['deviation_velocity'])

    #calculate min and max
    velocity_min = target_velocity - deviation_velocity
    velocity_max = target_velocity + deviation_velocity

    #close our file
    properties.close()

#Update our variables and run our feedback function
def update(_values):
    global distance,velocity
    distance = _values[3]
    velocity = _values[1]
    check_feedback()

#set our start_time, could also have used fbm.start_time = x on the wheelie.py script
def set_start_time(_t):
    global start_time
    start_time = _t

#Check if we want to give feedback
#currently only negative feedback is implemented but the same loop could be used for positive feedback
def check_feedback():
    #make sure we use our global variables (is only necessairy for variables that we are not redefining but restating all makes debugging easier)
    global ltime_slow,ltime_update, start_time
    global lines_slow, timeout_update,timeout_slow
    global distance,target_distance,velocity,velocity_min,velocity_max
    print(velocity_min)

    #Is it time to give feedback? And are we to slow?
    if ltime_slow + timeout_slow < time() and velocity < velocity_min:
        #reset the last time we gave feedback to current time
        ltime_slow = time()

        #it is time for some feedback on the slow peformance, we are going to slow
        print("snips feedback: go faster")
        #use our snipssay.py to send TTS messages
        snips_sayx("Your current speed is", round(velocity))
        #select random feedback line from lines_slow
        snips_say(lines_slow[randrange(len(lines_slow))])

    #Check if it is time for a status update
    if ltime_update + timeout_update < time():
        #reset the last time we gave feedback to current time
        ltime_update = time()

        #calculate progress and sent it to Snips TTS
        progress = int(100*distance/target_distance)
        mssg= "you are on " + str(progress) + " percent"
        snips_say(mssg)

        #calculate average speed and send it to Snips TTS
        avg_velocity = round(distance/(time()-start_time),1)
        snips_sayx("your average speed is ", avg_velocity)

#returns our properties dictionary that we read from config.txt
def get_properties():
    return d
