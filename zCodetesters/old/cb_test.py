import time
import callbacks
list = [["1","2","3"],["4","5",'6']]
print(list)
pr=list[1]
print(pr[2])
pr=str(time.strftime("%d_%m_%H%M%S", time.gmtime()))+'.csv'
cb = callbacks
print(cb.test)
