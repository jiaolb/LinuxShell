#!usr/bin/python
# -*- coding: UTF-8 -*-

x = 3.14
y = -3.14
m = 999
n = -999

print (u'1.将x转换为一个整数')
print (x,'->',int(x))

#print ('\r\n', u'2.将x转换为一个长整数')
#print (x,'->',long(x) )

print ('\r\n', u'3.将x转换为一个浮点数')
print (n,'->',float(n))

print ('\r\n', u'4.创建一个复数')
print (x,y,'->',complex(x,y))

print ('\r\n', u'5.将对象 x 转换为字符串')
print (x,'->',str(x))

print ('\r\n', u'6.将对象 x 转换为表达式字符串')
print (x,'->',repr(x))

print ('\r\n', u'7.计算字符串中有效的Python,并返回一个对象')
print ('eval(\'11+2\')','->',eval('11+2'))

print ('\r\n', u'8.将序列转换为元祖')
print ([m,n],'->',tuple([m,n]))

print ('\r\n', u'9.将序列转换为列表')
print ([m,n],'->',list([m,n]))

print ('\r\n', u'10.转换为可变集合')
print ([m,n],'->',set([m,n]))

print ('\r\n', u'11.转换为不可变集合')
print ([m,n],'->',frozenset([m,n]))

print ('\r\n', u'12.创建一个字典')
s1 = ('key',2)
s2 = ('value',3)
print (('key','value'),'->',dict((s1,s2)))

x = 0x31
print ('\r\n', u'13.将一个整数转换为一个字符')
print (x ,'->', chr(x))

#print ('\r\n', u'14.将一个整数转换为Unicode字符')
#print (x ,'->', unichr(x))

print ('\r\n', u'15.将一个字符转换为它的整数值')
print ('1' ,'->', ord('1'))

print ('\r\n', u'16.将一个整数转换为一个十六进制字符串')
print (31 ,'->', hex(31))

print ('\r\n', u'17.将一个整数转换为一个八进制字符串')
print (31 ,'->', oct(31))

print (31 ,'->', 0o31)

print (31, '->', bin(31))


print (u'type函数')
print (type(x))




