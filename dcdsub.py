#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
import time
import csv
from dotenv import load_dotenv  # To load the environment variables from the .env file
# DCD Hub
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from random import random


#print("Please give csv name (defaultdata): ")
#csvName = input() + '.csv'


# The thing ID and access token

# UUID of the GATT characteristic to subscribe


# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random
def setup():
    load_dotenv()
    global THING_ID,THING_TOKEN,BLUETOOTH_DEVICE_MAC,csvName,GATT_CHARACTERISTIC_ORIENTATION,my_thing,my_property

    THING_ID = os.environ['THING_ID']
    THING_TOKEN = os.environ['THING_TOKEN']

    csvName ='defaultdata.csv'

    #bluetooth max & UUID of gatt service
    BLUETOOTH_DEVICE_MAC ="F4:36:23:1E:9E:54"
    GATT_CHARACTERISTIC_ORIENTATION ="02118833-4455-6677-8899-AABBCCDDEEFF"

    my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
    my_thing.read()
    print(my_thing.to_json())
    my_property = my_thing.find_or_create_property("Wheelchair Speed",
                                                   PropertyType.THREE_DIMENSIONS)

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
    try:
        print("Received data: %s (handle %d)" % (str(value_bytes), handle))
        values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
    except:
        print("Could not convert data")
    try:
        write_csv(values)
    except:
        print("Could not write csv")
    try:
        writeto_dcd(values)
    except:
        print('dcd write function is not working')

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
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)

#=============================== CSV CLASSES=============================
def create_csv():
    try:
        with open (csvName,'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['theta', 'v','t'])
            csvFile.close
            print('Created csv file: '+ csvName)
    except:
        print('failed to create:')
        print(csvName)

def write_csv(csvData):
    try:
        with open(csvName, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(csvData)
            csvFile.close()
    except:
        print("could not write to csv")
def writeto_dcd(dcdData):
    print("Writing to dcd")
    my_thing.find_or_create_property("Wheelchair Speed",PropertyType.TWO_DIMENSIONS).update_values((dcdData[1],0))
    my_thing.find_or_create_property("Speedy wheelcair",PropertyType.ONE_DIMENSION).update_values((dcdData[1],))

    #my_property.update_values(dcdData)

# Instantiate a thing with its credential, then read its properties from the DCD Hub
#my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
#my_thing.read()
setup()
# Start a BLE adapter
bleAdapter = pygatt.GATTToolBackend()
bleAdapter.start()

# Use the BLE adapter to connect to our device
a = 1
b = 1
c = 1
d = 0

#Connect bluetooth device
while a:
    try:
        left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)
        print("Connection succesfull:" +str(BLUETOOTH_DEVICE_MAC) )
        a = 0
    except:
        print("whooopie daisy no connection")
        time.sleep(5)

#create our csv
create_csv()

# Subscribe to the GATT service
while b: #try this for 30 times
    try:
        print("try data subscribe")
        left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                         callback=handle_orientation_data)
        b = 0
    except:
        print("Trying to figure stuff out" + str(d))
        d = d + 1
        if(d>=30):
            b = 0
        time.sleep(1)

while True:
    time.sleep(1)

# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
