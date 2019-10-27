import serial
import time
import testsub
from snipssay import snips_say
import analysedata
ad = analysedata

if ad.checkd(100,10)=="slow": snips_say("Go faster")
time.sleep(3)
if ad.checkd(100,10)=="slow": snips_say("Go faster")
time.sleep(3)
if ad.checkd(200,10)=="good": snips_say("Nice keep going")
time.sleep(3)
if ad.checkd(200,10)=="good": snips_say("Nice keep going")
'''
print("check 50:", ad.check(50))
print("check 300:", ad.check(300))
print("check 200:", ad.check(200))
print("check 220:", ad.check(220))
if ad.check(200):
	print("whoop whoop")
if not ad.check(100):
	print("whoop whoop")
'''
'''
#test snips say
for i in range(10):
	snips_say(str(i))
	time.sleep(3)
'''
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
