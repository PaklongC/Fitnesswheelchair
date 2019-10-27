from time import time
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
def checkd(val,timeout):
    if last_time + timeout > time():
        global last_time
        last_time = time()
        if check(val):
            return "good"
        return "slow"
    print("not so fast")
    return ("wait")
