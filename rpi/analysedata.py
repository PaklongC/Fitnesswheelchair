from time import time

#simple data analyse script, check if the value is greater then min values
start_time = time()
last_time = start_time
target = 200
deviation = 20
min = target-deviation
max = target+deviation
#check value when function is called and return true/false
def check(val):
    global max,min
    if val >= min :
        #we are on/fasteher then target
        print("true", val)
        return True
    return False
#check value with a cooldown instead of true false return "good","slow" or "wait"
def checkd(val,timeout):
    global last_time
    print(last_time+timeout)
    print(time())
    if  last_time + timeout < time():
        last_time = time()
        if check(val):
            return "good"
        return "slow"
    print("not so fast")
    return ("wait")
