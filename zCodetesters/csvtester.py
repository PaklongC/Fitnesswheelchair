import csv
from pathlib import Path
import os
csvpath=os.path.dirname(os.path.abspath(__file__))
csvpath =os.path.join(os.path.dirname(os.path.abspath(__file__)),"testFolder","test2.csv")
#csvpath = Path(__file__).parent.absolute().joinpath('testFolder').joinpath('tesp.csv')
print(csvpath)

with open(str(csvpath), 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow([3,2,1,0])
    csvFile.close()

try:
    with open('test2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([3,2,1,0])
        csvFile.close()
except:
    print("could not write to csv2")
