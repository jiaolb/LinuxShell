#!/usr/bin/python
# -*- coding: UTF-8 -*-

def Check(func):
    def innerfunc(para):
        print ("checking...")
        return func(para)
    print ("hello")
    return innerfunc

@Check
def printself(a):
    print (a)
    print ('hi')


# = Check(printself(a))

printself("ss")
