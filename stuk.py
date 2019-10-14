import time
import csv
t = 'test.csv'
t = str(time.strftime("%d-%m_%H%M%S", time.gmtime()))+'.csv'
print(t)
with open(t, 'wb') as csvFile:
    writer = csv.writer(csvFile)
csvFile.close()
