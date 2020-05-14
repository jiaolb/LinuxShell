#!/usr/bin/python
# -*- coding: UTF-8 -*-

#1
#import time

#print u'当前时间为', time.ctime(time.time())

#2
#import time as tt

#print u'当前时间为', tt.ctime(tt.time())

#3
#from time import time,ctime

#print u'当前时间为', ctime(time())

#4
#from time import *

#print u'当前时间为', ctime(time())

import time

content = dir(time)
print (content)