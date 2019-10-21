from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from random import random

from dotenv import load_dotenv

import os
import time
# The thing ID and access token
load_dotenv()

THING_ID = 'dcd:things:wheelchair_speed-e706'
THING_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzEzODg4NzksImV4cCI6MTg4Njk2ODQ3OSwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.VweBCop25V8boYHcU6OMKf710K3yIUO1c2HgxLRcy8ziahW9tU9CCi9D5AZhJwRcnLS4Fy2WDGJsFrv29GrEAQx0RTVd1rc8ZAXXbokKtPnXAsVNVicdaYmi2nN2Q-1X7VtLMA5LVq1FA76KvlGo1nGe2lGIpAqgZxVtgL596GhfsWf4dcNk8qABVYZdkiPp5mNAX4iE42LUG59anUYY951cD5Wt31BhFKNU99CmuPFCUrXKkCzH1SoVHYkwfWuUBYD6j5FJdQZt7jdFEKfAUbl5vVn4eNkJITo8OY325YGuLcza6_uFl9Ve8XcLPuA3csipYV1oTz4ZIPcqk1C66I8NI_KEh0lIVqgPaV_3ZkPJR-3_Qc9UAbcXu1r0-J5AJDXXF6gA_IFSZkvdPtn73OgqnZEQauVdc9FOp6SCy2xdzddIXo02MnV1YkVdyWXgjygXdNjsPKVJQmurjHrikjZHfMFa7hCcJl-UFbBmeHoJ7syhQnoZ91dF7oG93U8Q9NsLgDdMjgnWmMmHBOytCwulO0C76RER2IjBS2aNfgRdWzGvMWO_QqWVZBqbuKzYc3qcqcH8rPaIN3IST6rg3zVWc7I5Nbq9a7_yomc7r6B_UfOzWjMI1x8NTPz7HyAYc5m3dfBpXOxK2Z-6O5xnOuUQQrEM9147N6E8OvQpyDk'

# Instantiate a thing with its credential
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

# We can fetch the details of our thing
my_thing.read()

print(my_thing.to_json())

# If we have no properties, let's create a random one
my_property = my_thing.find_or_create_property("My Random Property",PropertyType.THREE_DIMENSIONS)

                                               # Let's have a look at the property, it should

# Let's create a function that generate random values
def generate_dum_property_values(the_property):
    # Define a tuple with the current time, and 3 random values
    values = (random(), random(), random())
    # Update the values of the property
    the_property.update_values(values)
# Finally, we call our function to start generating dum values
while True:
    generate_dum_property_values(my_property)
    # Have a 2-second break
    time.sleep(2)

# contains the name, a unique id and the dimensions
print(my_property.to_json())
