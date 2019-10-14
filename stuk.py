import time
import csv
t = 'test.csv'
t = str(time.strftime("%d-%m_%H%M%S", time.gmtime()))+'.csv'

print("Please give csv name (defaultdata): ")
t = input() + '.csv'
if t =='.csv':
    t = 'defaultdata.csv'
print(t)
with open(t, 'wb') as csvFile:
    writer = csv.writer(csvFile)
csvFile.close()
