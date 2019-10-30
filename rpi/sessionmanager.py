from snipssay import snips_say, snips_sayx
from time import time
from random import randrange
distance=0
target_distance=
velocity=0
target_velocity= 200
deviation_velocity=20
velocity_min = target_velocity - deviation_velocity
velocity_max = target_velocity + deviation_velocity
start_time = time()
ltime_update = time()
ltime_positive = time()
ltime_slow = time() + 10
lines_slow = ["try going faster", "You are a bit to slow", "Keep it up go faster", "GO GO GO"]
class session:
  def __init__(self, duration, target,deviation,velocity,distance,time):
    self.duration = 60
    self.target = 200
    self.deviation = 20
    self.velocity

def update_values(_values):
    global distance,velocity
    distance = _values[3]
    velocity = _values[1]
    check_actions()
def check_actions()
#feedback timeouts in seconds
    timeout_update=60
    timeout_slow=20
    global ltime_slow,ltime_update, start_time
    global distance,target_distance,velocity,velocity_min,velocity_max
    if ltime_slow + timeout_slow < time() and velocity < velocity_min:
        ltime_slow = time()
        ltime_update = time() + 5 #wait 5 more seconds before allowing feedback
        #it is time for some feedback on the slow peformance, we are going to slow
        snips_sayx("Your current speed is", velocity)
        snips_say(lines_slow[randrage(len(lines_slow))])
    if ltime_update + timeout_update < time():
        progress = 100*distance/target_distance
        mssg= "you are on" + progress + "precent"
        snips_say(mssg)
        avg_velocity = distance/(time()-start_time)
        snips_sayx("your average speed is", avg_velocity)
