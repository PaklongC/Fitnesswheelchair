from random import random
import time

from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType

from dotenv import load_dotenv
import os
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['my-wheelchair-bf59']
THING_TOKEN = os.environ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1Njg5NzExNjksImV4cCI6MTg4NDU1MDc2OSwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.Ta4Vafyd4ENU8yb7NuZQlU08b-h1HAM9_ZBQhGWWTA4sRrsT2PM2ISSyiAeWsKi-qR6-0fOXHSZIuCdjU_N4nyEAXef9_ZgxKwlJRsc4UQBHqpXcTUtNGbnjDL6kBeOjWRf6VXkAJ3t5u2i0dFi7BHbMorpnz0PmPtGTC8_bqqkqtKfv79xqQ67PdeBa7_O_9M8DaKZdyRzXfNy62HcmmHf1MltBGOaBc4yr20p7OiEy4QKRsctnFkjnyrVYsG5jaN1m3PM4c406afv_bjr0OIGmM0dv2FZA3hTH7FdzogXTEL8YIEvoo_T8INaGsVnZ16QhBRE-52WZSafBRMrdkzxt6aUBBbzCjtkelVVqTs3ze45EBGBOmLD3Ri4t8BhiR8HvcJ85qJOs1OmpTUqw_Ea_3-IteTHwKvX8WjedTXx0LRz4K6rZRto_7VJzm71UxQORLFziT_BdIVZ54Zkl233lZIM7DrdeyCdxNkkQuhI-UeJaaMIzjhRRAXhuYvU1Yd2cVH9KyfIdXPbR_Mz_XinTjuwj6YqIkfnNr8nUf6GkIzlJ2ja4E25HzfEPVjhPgcFmhxVOZrM_OnCOPyL013LLPiJ6Mlwhy9ISsB1g53VPt2V4frXySQS5vmsiVsyd9w9tx9Lw6Ox669n_yFwfeLH5R90lcgiNg7twGntq6pg']
# Instantiate a thing with its credential
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

# We can fetch the details of our thing
my_thing.read()

print(my_thing.to_json())

# If we have no properties, let's create a random one
my_property = my_thing.find_or_create_property("My Random Property",PropertyType.THREE_DIMENSIONS)

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
