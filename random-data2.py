from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from random import random

from dotenv import load_dotenv

import os
import time
# The thing ID and access token
load_dotenv()

THING_ID = 'my-test-thing-e1fc'
THING_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzA0MzU2MDcsImV4cCI6MTg4NjAxNTIwNywiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.RjcUPyZ-lGm_2lixiHNcZDjD_fyvAqXXTK_ahXQ37szduH6l99ShCN2UZ6mvxb6_JskjmShM9-tO4Iq3p5gW3RYe6IKV9iIcWxU34waex9_bqd7j1Yiw0IUE7sRp2C-30p1zQYhemmJ5yvRf1IQNh9qjkUPI8_EEBxNHiKSCFZnMq4M5Kiaq1V7XlrFJbraXgI4iB2Pg1N9UyFvqncaiuP-YX50TSWSgnZSUX-CLYCs8gU_MwYv2Jr_BYQmQgcwRj78RJ-0s45DK446dQXjmA-RF5GMeHjRlkvOfJ4FH0fWgyzhduqTnSGRli273c9ouButWGDIAeUy9zpfMcLNaNKfMwAzm-6NtYXHy0fxcu6gaO4JZjY5ItzJQfYRXb9tEUKTFCY3LcctoDoVXSBhNCrOQbuMY-k459iy_UoLmQRWNZr8zVUMb4ORsl3kYB_JIb8VSUbhw-BvUHU7NL2D3kLyCz0IuWOmq5bllWHOgSkXYcqyhyzJWmtt1-xeedF3rH-vD9aWP9AHSmC1WvL6p2k8KjMQiVeL-fYz6hmJC_S-ZA3-Q31KDzMDti9vsYRE4hyh-U-9LbK_gqh-XlMYJVuzqOH__XTxLd-V5MEus6PCCruOw7KJ_t8pVOPoqiHxZlpwalv7oN_N-ioB3X3E_brsTw51_WLMey2_xBjnidfU'
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
