#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

#返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time_sec_1 = time.time()
print (u'当前时间戳', time_sec_1)
print (type(time_sec_1))

print (isinstance(time_sec_1, float))

#接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t
time_1 = time.localtime(time_sec_1)
print (u'当前时间为', time_1)
print (type(time_1))
print (isinstance(time_1, time.struct_time ))

print (time.mktime(time_1))

#接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
time_2 = time.asctime(time_1)
print (u'当前时间为', time_2)

#作用相当于asctime(localtime(secs))，未给参数相当于asctime()
time_3 = time.ctime(time_sec_1)
print (u'当前时间为', time_3)

#用以浮点数计算的秒数返回当前的CPU时间
time_sec_2 = time.clock()
print (u'当前时间戳', time_sec_2)

#接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
print (u'当前时间为', time.strftime("%Y-%m-%d %H:%M:%S Week%w", time.localtime()))
print (u'当前时间为', time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

#根据fmt的格式把一个时间字符串解析为时间元组。
a = "Sat Mar 28 22:24:24 2016"
print (time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

print(time.localtime(0))












