import csv
from pathlib import Path

csvpath = Path(__file__).parent.absolute().joinpath('testFolder').joinpath('tesp.csv')
print(csvpath)

with open(str(csvpath), 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow([3,2,1,0])
    csvFile.close()

print("could not write to csv1")
try:
    with open('test2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([3,2,1,0])
        csvFile.close()
except:
    print("could not write to csv2")
