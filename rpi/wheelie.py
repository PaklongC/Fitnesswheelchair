#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os,shutil  # To access environment variables
import time
import csv
import analysedata, feedbackmanager

from threading import Thread
from dotenv import load_dotenv  # To load the environment variables from the .env file
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from random import random
from dotenv import load_dotenv
from snipssay import snips_say
from pathlib import Path
from datetime import datetime

#============================= Setup =====================================
#Run this first & declare all global variables
def setup():
    load_dotenv()
    global THING_ID,THING_TOKEN,BLUETOOTH_DEVICE_MAC,ADDRESS_TYPE,GATT_CHARACTERISTIC_ORIENTATION,bleAdapter
    global my_thing,my_property,csvName, dataPath
    global start_time, dcd_start_time
    global ad, distance, fbm, collecting
    collecting = True
    ADDRESS_TYPE = pygatt.BLEAddressType.random
    THING_ID = os.environ['THING_ID']
    THING_TOKEN = os.environ['THING_TOKEN']

    csvName ='defaultdata.csv'
    dataPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","defaultdata.csv")
    #bluetooth max & UUID of gatt service
    BLUETOOTH_DEVICE_MAC ="F4:36:23:1E:9E:54"
    GATT_CHARACTERISTIC_ORIENTATION ="02118833-4455-6677-8899-AABBCCDDEEFF"

    bleAdapter = pygatt.GATTToolBackend()
    bleAdapter.start()

    my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
    my_thing.read()
    #print(my_thing.to_json())
    my_property = my_thing.find_or_create_property("Wheelchair Speed",
                                                   PropertyType.THREE_DIMENSIONS)
    start_time = time.time()
    dcd_start_time = datetime.now()

    ad = analysedata
    distance = 0
    fbm = feedbackmanager
    print(" get config")
    #print(fbm.getConfig())
#=============================== Bluetooth CLASSES=============================

def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)


def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    if(collecting):
        try:
            global ad, distance, values
            #print("Received data: %s (handle %d)" % (str(value_bytes), handle))
            values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
            #speed m/s to km/h
            values[1]= 3.6*values[1]
            distance += abs(values[2]) #FIXME arduino code distance is nu negatief
            values.append(distance)
            print(values)
        except: print("Could not convert data")
        try: fbm.update(values)
        except: print("feedbackmanager failed")
        try: write_csv(values)
        except: print("Could not write csv")
        try: writeto_dcd(values)
        except: print('Could not send data to dcdhub')

    #find_or_create("Left Wheel Orientation",
                #   PropertyType.THREE_DIMENSIONS).update_values(values)


def discover_characteristic(device):
    """List characteristics of a device"""
    for uuid in device.discover_characteristics().keys():
        try:
            print("Read UUID" + str(uuid) + "   " + str(device.char_read(uuid)))
        except:
            print("Something wrong with " + str(uuid))


def read_characteristic(device, characteristic_id):
    """Read a characteristic"""
    return device.char_read(characteristic_id)


def keyboard_interrupt_handler(signal_num, frame):
    """Make sure we close our program properly"""
    print("Exiting...".format(signal_num))
    #global left_wheel
    #left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    if(collecting):
        stop_session()
    exit(0)

#=============================== CSV CLASSES=============================
def create_csv():
    try:
        with open (dataPath,'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['theta', 'v','darc','distance'])
            csvFile.close
            print('Created csv file: '+ csvName)
    except:
        print('failed to create:')
        print(csvName)

def write_csv(csvData):
    try:
        with open(dataPath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(csvData)
            csvFile.close()
    except:
        print("could not write to csv")
def writeto_dcd(dcdData):
    #print ("sending data to dcd")
    my_thing.find_or_create_property("Rotation",PropertyType.TWO_DIMENSIONS).update_values((dcdData[0],dcdData[1]))
    my_thing.find_or_create_property("Speed",PropertyType.ONE_DIMENSION).update_values((dcdData[1],))
#try connecting to BLUETOOTH_DEVICE_MAC if not able to connect try again
def connect_bluetooth():
    a=1
    while a:
        print('start connecting to:', BLUETOOTH_DEVICE_MAC)
        snips_say("start connection")
        try:
            global left_wheel
            left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)
            print("Connection succesfull:" +str(BLUETOOTH_DEVICE_MAC))
            create_csv()
            a = 0

        except:
            print("whooopie daisy no connection")
            time.sleep(5)

    #subscribe to bluetooth service with UUID
    b = 1
    d = 0
    time.sleep(2)
    #subscribe gatt service
    try:
        print("subscribing to service")
        left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                         callback=handle_orientation_data)
    except:
        print("could not subscribe to gatt service")
        time.sleep(5)
        left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION,wait_for_response=False)
        bleAdapter.stop()
        bleAdapter.start()
        connect_bluetooth() #try to connect again
#Connect bluetooth device
def start_connection():
    setup()
    connect_bluetooth()
    snips_say("setup complete, Let's start rolling")
    global start_time, dcd_start_time
    start_time = time.time()
    dcd_start_time = datetime.now()
    fbm.set_start_time(start_time)
    #keep thread open
    #while True:
    #    time.sleep(1)
        #print('sleeping')
def start_data_collection():
    try:
        print('started connection & data collection thread')
        global thread
        thread = Thread(target=start_connection)
        thread.start()
    except:
        print('could not start thread')
def stop_session():

    #global left_wheel, collecting,  distance, start_time
    global collecting
    end_time = time.time()
    dcd_end_time = datetime.now()
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION,wait_for_response=False)
    collecting = False
    print("stop session")
    print("Analysing data")
    #save session   name,avg_velocity,target_velocity,start_time,end_time,distance,target_distance
    session_name = "workout_"+str(time.strftime("%d_%m_%H%M%S", time.gmtime()))+'.csv'
    avg_velocity = round(distance/(end_time-start_time),1)
    session_info=[session_name,avg_velocity,fbm.target_velocity,start_time,end_time,distance,fbm.target_distance,datetime.strftime(dcd_start_time,"%Y-%m-%d %H:%M:%S"),datetime.strftime(dcd_end_time,"%Y-%m-%d %H:%M:%S")]
    print(session_info)
    try:
        sessionPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"session_index.csv")
        with open (sessionPath,'a') as s_csvFile:
            writer2 = csv.writer(s_csvFile)
            writer2.writerow(session_info)
            s_csvFile.close
            print("wrote session info:",sessionPath, "to:",session_info)
            #print('saved session data: '+ session_info)
    except:
        print('failed to save session data')
    #copy our session data to another csv
    try:
        new_dataPath =os.path.join(os.path.dirname(os.path.abspath(__file__)),"data",session_name)
        print("copy data to:",new_dataPath)
        shutil.copyfile(dataPath,new_dataPath)
    except:
        print("could not copy data: ",dataPath," to: ",new_dataPath)

    try:
        if avg_velocity >= target_velocity :
            print("Good job")
            '''
            mssg="Good job"
            snips_say(mssg)
            mssg="Your average speed over" + distance + " meters"
            snips_say(mssg)
            mssg="was" + avg_velocity
            snips_say(mssg)

        else:
            snips_say("You tried well better luck next time")
            mssg="Your average speed over" + distance + " meters"
            snips_say(mssg)
            mssg="was" + avg_velocity + "kilometers per hour"
            snips_say(mssg)
            mssg="Unfortunately you did not reach the target speed of" + fbm.target_velocity + " kilometers per hour"
            snips_say(mssg)

'''
# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
