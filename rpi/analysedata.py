from time import time
from snipssay import snips_say
start_time = time()
last_time = start_time
target = 200
deviation = 20
min = target-deviation
max = target+deviation
def check(val):
    global max,min
    if val >= min :
        #we are on/fasteher then target
        print("true", val)
        return True
    return False
def check_say(val,timeout,message):
    if last_time + timeout > time():
        last_time = time()
        if not check(val):
            snips_say(message)
    else
        print("not so fast")
