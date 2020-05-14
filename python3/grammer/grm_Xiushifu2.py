#!/usr/bin/python
# -*- coding: UTF-8 -*-

def decorated_by(func):
    func.__doc__+='\nDecorated by decorated_by.'
    return func

@decorated_by
def add(x,y):
    '''Return the sum of x and y'''
    return x+y

if __name__ == '__main__':
    add(1,2)