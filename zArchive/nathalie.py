#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import logging
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
from dotenv import \
    load_dotenv  # To load the environment variables from the .env file

#Keyboard functions
from pynput.keyboard import Key, Controller
import time


logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)


keyboard=Controller()

time.sleep(1)

## DCD Hub
# from dcd.entities.thing import Thing
# from dcd.entities.property import PropertyType



# The thing ID and access token
#load_dotenv()
#THING_ID = os.environ['THING_ID']
#THING_TOKEN = os.environ['THING_TOKEN']
BLUETOOTH_DEVICE_MAC = "de:f7:c5:c8:80:4f"
#os.environ['BLUETOOTH_DEVICE_MAC']

# UUID of the GATT characteristic to subscribe
GATT_CHARACTERISTIC_ORIENTATION = "02118833-4455-6677-8899-AABBCCDDEEFF"

# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

started_timer = False


def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)


def timer(n):

    if (started_timer == False):
        start_time = time.time()
        started_timer = True
    else:
        time_of_check = time.time()
        time_diff = time_of_check - start_time
        print("time difference: " + time_diff)
        if (time_diff > 19000):
            start_time = time.time()
            print("Time reset")


def handle_orientation_data(handle, value_bytes):
    i = 30
    #print("bugfix 03")
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    #print("Received data: %s (handle %d)" % (str(value_bytes), handle))
    #print("Recieved data: " + (str(value_bytes)))
    #print("bugfix 04")
    #while (blue_con == True):
        #try:
    #print("bugfix 05")
            #print("value bytes:   ")
            #print(value_bytes)
            #print("hello")

    try:
                #print("bugfix 06")
        values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
        #print("bugfix 07")
        #print(values)
    except:
        raise Exception('No values coming in')
        #print("bugfix 08")
                #print("everything is going wrong")

        #except:
            #print("Something went terribly wrong but at least we can display it")
            #print("bugfix 09")
            #from values to typing
    if (values[0] > 500 and values[2] < 400):

        print("Going right")
                #time.sleep(1)
        keyboard.press(Key.right)

        #time.sleep(0.01)
        #keyboard.release(Key.right)
        #print("bugfix 11")
    elif (values[2] > 500 and values[0] < 400):

        print("Going left")
        #time.sleep(1)
        keyboard.press(Key.left)
        #time.sleep(0.01)
        #keyboard.release(Key.left)
        #print("bugfix 13")
        #left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
        #print("unsub")
        #exit(0)
    elif values[1] > 70:

        print("JUMP")
        keyboard.press(Key.space)
        #print("bugfix 15")

    else: #(values[2] < 400 and values[0] < 400 and values[1] < 400):

        print("Do nothing")
        keyboard.release(Key.right)
        keyboard.release(Key.left)
        #print("bugfix 17")

    #print("before the timer")
    #timer()



#    find_or_create("Left Wheel Orientation",
#                   PropertyType.THREE_DIMENSIONS).update_values(values)


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
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)


# Instantiate a thing with its credential, then read its properties from the DCD Hub
# my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
# my_thing.read()

# Start a BLE adapter
bleAdapter = pygatt.GATTToolBackend()
bleAdapter.start()

# Use the BLE adapter to connect to our device

a = 1
i = 10
while a:
    try:
        left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)
        print("we are connected!")
        a =0
    except:
        print("No connection")

# Subscribe to the GATT service
try:
    left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION, callback=handle_orientation_data)

except:
    print("Can't subscribe to bluetooth")
while True:
    time.sleep(1)
# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
