from random import random
import time

from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType

from dotenv import load_dotenv
import os
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['my-wheelchair-3762']
THING_TOKEN = os.environ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1Njg5NjUwMzIsImV4cCI6MTg4NDU0NDYzMiwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.xcfxUXqNJJhEZi5BKC1yxgPz6V6_sJwqN_Jk9u_CGC0uYtwlI4lmZzh39C4UB7RJTeiFJpgciDw863hpkVqo2wUPPUtbuoyRm0yr3F6BPE5frB_1igfaUkJnxa-JYVdZsq9T0Kjaal3HN0j_Caqd-jF1akOYj3Z--8PvK-No1uh41QpmAGecMTK_aqvFgfKaao8DE36OBMeDPARd9ou7sZN89nWXXlM-3huW9S_hzcAS_DgA6qmsYf07EzSNp3folfsFASwVHrjSbYh1kzi3aAfLg81UQoAE6XEyGEX4Q-O_ByQROmVpe6PRphD2qmZq52KW3ORv-8EzUCn-F665HeYu5qJxeuT4AsFUk-egkdP7hPU3-EvPf74uycSsnL2c30WyTxfgilG65Ld__v30oa922_oU3xPUbyfYYm-PXA-snqKujZykvahV_Kd0OGrWlZ7aZL3aM47614xqSpHyYG0J_JrwxBvVCggthgVJxr46Kw2hkFtfJvUcA2K2g-zaB9s1Sno01mncM_I0kAfgAqNr18bSd5AJQkT6V9fn2zdEfd5evpj06EDBoex3tc-YuHIB9f1u0LgLWzAJGomYWBPbUf56Y-mTuy-GOfxyUZCFD0vy951T8w35Av_B2shQTeCUUycAGf888XHMszsdarXcYWliYM6g2lOjX0wuhIE']

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
