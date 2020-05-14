#!usr/bin/python
# -*- coding: UTF-8 -*-

#变量赋值
counter = 100
miles = 1000.0
name = 'John'

print ('1.' + u'变量赋值举例:')
print (counter)
print (miles)
print (name)

#多个变量赋值
print ('\r\n2.' + u'多个变量赋值:')
a = b = c = 1
print (a,b,c)

a,b,c = 1,2,'John'
print (a,b,c)

#变量删除
del a,b,c
#print a,b,c

#列表类型
print ('\r\n3.' + u'列表类型:')
list1 = ['pi', '=', 0]
list1[2] = 3.1415926
print (list1[0],list1[1],list1[2])

#元祖类型
print ('\r\n4.' + u'元祖类型:')
tuple = ('pi', '=', 3.1415926)
#tuple[2] += 0.0000001
print (tuple[0],tuple[1],tuple[2])

#字典
print ('\r\n5.' + u'字典类型:')
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (tinydict['name'])
print (tinydict.keys())

