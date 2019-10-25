import time

def ftest():
    global s,a,c
    s = "global test"
    a = " aaa"
    c = "cccc"
def ft2():
    global s
    print(s)
    print(c)
    s = "local to global"
ftest()
print(s)
ft2()
print(s)
print(a)
'''
##Test counter###
i =2
print('test'+ str(i))
def counter():
    i = 0
    while i <=10:
        i = i + 1
        print(i)
        time.sleep(1)
    print("test")
def stopfunction():
    print('stop!')
print("test213124")
counter()
'''
