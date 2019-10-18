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

# The thing ID and access token
load_dotenv()
THING_ID = 'dcd:things:wheelchair_speed-e706'
THING_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzEzODg4NzksImV4cCI6MTg4Njk2ODQ3OSwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.VweBCop25V8boYHcU6OMKf710K3yIUO1c2HgxLRcy8ziahW9tU9CCi9D5AZhJwRcnLS4Fy2WDGJsFrv29GrEAQx0RTVd1rc8ZAXXbokKtPnXAsVNVicdaYmi2nN2Q-1X7VtLMA5LVq1FA76KvlGo1nGe2lGIpAqgZxVtgL596GhfsWf4dcNk8qABVYZdkiPp5mNAX4iE42LUG59anUYY951cD5Wt31BhFKNU99CmuPFCUrXKkCzH1SoVHYkwfWuUBYD6j5FJdQZt7jdFEKfAUbl5vVn4eNkJITo8OY325YGuLcza6_uFl9Ve8XcLPuA3csipYV1oTz4ZIPcqk1C66I8NI_KEh0lIVqgPaV_3ZkPJR-3_Qc9UAbcXu1r0-J5AJDXXF6gA_IFSZkvdPtn73OgqnZEQauVdc9FOp6SCy2xdzddIXo02MnV1YkVdyWXgjygXdNjsPKVJQmurjHrikjZHfMFa7hCcJl-UFbBmeHoJ7syhQnoZ91dF7oG93U8Q9NsLgDdMjgnWmMmHBOytCwulO0C76RER2IjBS2aNfgRdWzGvMWO_QqWVZBqbuKzYc3qcqcH8rPaIN3IST6rg3zVWc7I5Nbq9a7_yomc7r6B_UfOzWjMI1x8NTPz7HyAYc5m3dfBpXOxK2Z-6O5xnOuUQQrEM9147N6E8OvQpyDk'

BLUETOOTH_DEVICE_MAC ="F4:36:23:1E:9E:54"

# Instantiate a thing with its credential
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

# We can fetch the details of our thing
my_thing.read()
print(my_thing.to_json())

# UUID of the GATT characteristic to subscribe
GATT_CHARACTERISTIC_ORIENTATION ="02118833-4455-6677-8899-AABBCCDDEEFF"

# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random


                        #===BLUETOOTH===#


def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    try:
        print("Received data: %s (handle %d)" % (str(value_bytes), handle))
        values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
        my_property = my_thing.find_or_create_property("Speedy wheelcair",
                                                       PropertyType.ONE_DIMENSION).#update_values(values)

    except:
        print("Could not convert data")

def wheelchair_values(the_property):
    speed = values[1]
    the_property.update_values(speed)

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
    wheelchair_values(my_property)
    time.sleep(1)

print(my_property.to_json())

# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
