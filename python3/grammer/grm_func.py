#!/usr/bin/python
# -*- coding: UTF-8 -*-

def MyFunc(x=1, y=2, *plist, **pdist):
    'print x y list dist!'
    print (x)
    print (y)
    print (plist)
    print (pdist)
    
def MyFunc2(**pdist):
    print (pdist)
    

tmplist = [33,34,35]
tmpdist = {'name':'Tom', 'age':'33'}

MyFunc() 

MyFunc(5,) 

MyFunc(y=5,x=3)

MyFunc(2,3,22,44,'33',tmpdist)

MyFunc(2,3,(22,44,'33',tmpdist),'44')

MyFunc(2,3,22,44,i=1,you=2)

