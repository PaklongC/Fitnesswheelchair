import time

def counter(loop_on):
    i = 0
    while i <=10:
        if loop_on.value == True:
            i = i + 1
        print(i)
        time.sleep(1)
    print("test")
