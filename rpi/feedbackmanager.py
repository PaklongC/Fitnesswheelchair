from snipssay import snips_say, snips_sayx
from time import time
from random import randrange

global target_distance,target_velocity,velocity_min,velocity_max
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
lines_slow = ["try going faster", "You are a bit to slow", "go faster", "go go go","Atleast you are not standing still but try harder","are you even moving","are you even trying","I dont think you are trying","you are not a good roll model"]
#try:
def getConfig():
    with open("config.txt") as properties:
        l = [line.split("=") for line in properties.readlines()]
        p = {key.strip(): value.strip() for key, value in l}
        #global target_distance,target_velocity,deviation_velocity
        #print(p['target_distance'])
        target_distance = int(p['target_distance'])
        target_velocity= int(p['target_velocity'])
        deviation_velocity = float(p['deviation_velocity'])
        velocity_min = target_velocity - deviation_velocity
        velocity_max = target_velocity + deviation_velocity

        return p
    properties.close()
#except:
#    print("config werkt niet")
def update(_values):
    global distance,velocity
    distance = _values[3]
    velocity = _values[1]
    check_feedback()
def check_feedback():
#feedback timeouts in seconds

    timeout_update=60
    timeout_slow=20
    global ltime_slow,ltime_update, start_time
    global lines_slow
    global distance,target_distance,velocity,velocity_min,velocity_max
    print(velocity_min)
    if ltime_slow + timeout_slow < time() and velocity < velocity_min:
        ltime_slow = time()
        #wait 5 more seconds before allowing feedback
        #it is time for some feedback on the slow peformance, we are going to slow
        print("snips feedback: go faster")
        snips_sayx("Your current speed is", round(velocity))
        snips_say(lines_slow[randrange(len(lines_slow))])
    if ltime_update + timeout_update < time():
        ltime_update = time()
        progress = int(100*distance/target_distance)
        mssg= "you are on " + str(progress) + " percent"
        snips_say(mssg)
        avg_velocity = round(distance/(time()-start_time),1)
        snips_sayx("your average speed is ", avg_velocity)
