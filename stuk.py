#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
import time
from dotenv import \
    load_dotenv  # To load the environment variables from the .env file

##Keyboard functions
#from pynput.keyboard import Key, Controller
import time

#keyboard=Controller()

time.sleep(1)

## DCD Hub
# from dcd.entities.thing import Thing
# from dcd.entities.property import PropertyType



# The thing ID and access token
#load_dotenv()
#THING_ID = os.environ['THING_ID']
#THING_TOKEN = os.environ['THING_TOKEN']

#os.environ['BLUETOOTH_DEVICE_MAC']

# UUID of the GATT characteristic to subscribe
#ONS
BLUETOOTH_DEVICE_MAC ="F4:36:23:1E:9E:54"
GATT_CHARACTERISTIC_ORIENTATION = "02118833-4455-6677-8899-AABBCCDDEEFF"
#nathalie
#BLUETOOTH_DEVICE_MAC = "de:f7:c5:c8:80:4f"
#GATT_CHARACTERISTIC_ORIENTATION = "02118833-4455-6677-8899-AABBCCDDEEFF"

# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random


def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)

'''
def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    #print("Received data: %s (handle %d)" % (str(value_bytes), handle))
    #print("Recieved data: " + (str(value_bytes)))

    try:
        start = time.time()
        print("value bytes:   ")
        print(value_bytes)
        print("hello")

        try:
            values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
        except:
            raise Exception('No values coming in')
            #print("everything is going wrong")

    except:
        print("Something went terribly wrong but at least we can display it")
        #from values to typing
    if (values[0] > 500 and values[2] < 400):
        print("Going right")
        #time.sleep(1)
#        keyboard.press(Key.right)
        #time.sleep(0.01)
        #keyboard.release(Key.right)
    elif (values[2] > 500 and values[0] < 400):
        print("Going left")
        #time.sleep(1)
#        keyboard.press(Key.left)
        #time.sleep(0.01)
        #keyboard.release(Key.left)
    elif values[1] > 70:
        print("JUMP")
#        keyboard.press(Key.space)
    else:
        print("Do nothing")
#        keyboard.release(Key.right)
#        keyboard.release(Key.left)

'''

def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    print("Received data: %s (handle %d)" % (str(value_bytes), handle))
    values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
    #find_or_create("Left Wheel Orientation",
    #               PropertyType.THREE_DIMENSIONS).update_values(values)
    #except:
    #    print("its just a test")
    try:
        print(values[0])
    except:
        print("Ik kan dingen")
    #find_or_create("Left Wheel Orientation",
    #               PropertyType.THREE_DIMENSIONS).update_values(values)
    #except:
    #    print("its just a test")

'''
def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    try:
        print("data")
    except:
        print("poep")
    try:
        print("value bytes:   ")
        print(value_bytes)
        print("hello")
    except:
        print("het leven is kut")
    #find_or_create("Left Wheel Orientation",
    #               PropertyType.THREE_DIMENSIONS).update_values(values)
    #except:
    #    print("its just a test")

#    find_or_create("Left Wheel Orientation",
#                   PropertyType.THREE_DIMENSIONS).update_values(values)
'''

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

a = 1
b = 1
d = 0

# Use the BLE adapter to connect to our device
while a:
    try:
        left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)
        print("we are connected!")
        a = 0
    except:
        print("whooopie daisy no connection")
# Subscribe to the GATT service
print ("p1")
while b:
    try:
        print("try data")
        left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                         callback=handle_orientation_data)
        b = 0
    except:
        print("Trying to figure stuff out")
        d = d + 1
        if(d>=30):
            b = 1
        time.sleep(1 )
print("p2")
# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
