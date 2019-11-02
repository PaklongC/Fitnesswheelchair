from pathlib import Path
mypath = str(Path().absolute())
print(mypath)
#def getConfigs():
with open("configsx.txt") as properties:
    l = [line.split("=") for line in properties.readlines()]
    p = {key.strip(): value.strip() for key, value in l}
    global target_distance,target_velocity,deviation_velocity, velocity_min, velocity_max
    #print(p['target_distance'])
    target_distance = int(p['target_distance'])
    target_velocity = int(p['target_velocity'])
    deviation_velocity = float(p['deviation_velocity'])
    velocity_min = target_velocity - deviation_velocity
    velocity_max = target_velocity + deviation_velocity
    print(p)
    properties.close()
    #return p
#getConfigs()
'''
with open("t.properties") as properties:
    l = [line.split("=") for line in properties.readlines()]
    d = {key.strip(): value.strip() for key, value in l}
    print(d)
    print(l)

    print(d['a'])
    properties.close()

with open("config.txt") as properties:
    l = [line.split("=") for line in properties.readlines()]
    p = {key.strip(): value.strip() for key, value in l}
    #global target_distance,target_velocity,deviation_velocity
    print(p['target_distance'])
    target_distance = p['target_distance']
    print(p['target_velocity'])
    deviation_velocity = p['deviation_velocity']
        #velocity_min = target_velocity - deviation_velocity
        #velocity_max = target_velocity + deviation_velocity
        #pr = "porperties set: " + "TD:"+ target_distance + "TV:" + target_velocity + "DV:" + deviation_velocity
        #print(pr)
    properties.close()
'''
