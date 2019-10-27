import serial
import time
import testsub
from snipssay import snips_say

for i in range(10):
	snips_say(str(i))
	time.sleep(3)

'''
#counter in other script test
t = testsub

for i in range(6):
	print(i)
	t.count()
	print(time.time())
	time.sleep(2)
for i in range(6):
	print(i)
	t.count()
	print(time.time())
	time.sleep(2)
'''
