#!usr/bin/python
# _*_ coding:UTF-8 _*_

try:
    print (3/0)
except ZeroDivisionError:
    print (3//1)
finally:
    print (1)
    
try:
    print (3/0)
except:
    print ('something wrong happen!')
finally:
    print (1)

class somethingerr(Exception):
    def __init__(self, arg):
        self.Func = arg
        self.Func()

def printmyself():
    print ("ssss")

try:
    raise somethingerr(printmyself)
except somethingerr:
    print ('something error done')
    