from random import random
import time

from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType

from dotenv import load_dotenv
import os
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['my-wheelchair-4996']
THING_TOKEN = os.environ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjkyMjc1MjcsImV4cCI6MTg4NDgwNzEyNywiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.iTfJ_kXXBgRmKxlJ80uvnPCUfE6vqRAY8XKnsrgtgum5AcgO9InFdbniKVDo-Oz0rhHtMmurzdhywEFJXBbdQ4nPxRki-KgyhoNulwdVyJlPiByinvHIRYymyWdMo4_mQg9e6Fmvk7vewKSEgK7IslBtK7tlDUmk2Ig1h0-1iIYMpwXkE0nvVY4XPRVea88A_CdHhLish3eYYlV-uXlCMyQTw4uOdUjMZ3uXCUL2txOht63vPtMO-nBeuuCJois5N8Z8imhsKK9lGCAWei9TxcPTar13tE52HWQm3BsONpoRHjsdlvOD87Y5eS_AR-VwYJZOV9PzQD0lHCwoWg3s_aQsW53j04Ec7Sl_gfOyD_YAr_jcU-0E2MErn7qHEU1lxzdM_fWMpmgkDtRvyNS83oDsnPlZRV-VIPd5Sk9JLsBkCSpbpI0Dj2BheF7oZSDcNB4Dd02TXomqQYaWTWhle96rMSp-vGWUHP1Ix3HU8Ew6jbuDMykO5vqUiE_29B79p3u0sDBQKQ_4HgL3KcsnO6rQp0EuIX2J70IknRHf2mm0w-cnYm76PSLVAbweGiDq2DzjgbpwoO_YpVmroUOQi5ZBKTROf6C4M6PO9UX5leoKQk5U9UfsFmmviqs07UGQYVOeHMf0hyCsyuMKkF-CJ8Br6wSqpQX1MpSnSgq793Y']

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
