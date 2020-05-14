#!usr/bin/python
# _*_ coding: UTF-8 _*_

x = -1.5
y = 1.0

#类型转换
print (int(x))
#print (long(x)) #Python3取消了long
print (str(x))
print (str(int(x)))
print (float(int(x)))
print (int('22'))
print ('\n')

i = float('2.22')
print (i)

#进制转换
print (hex(49))
print (hex(0x31))
print (oct(49))
print ('\n')

#复数类型
z = complex(12,34)
print (z)
print (str(z))
print (repr(z))

#字符串转换
m = 0x31 #ASCII - '1'
print (chr(m))

print ([u'焦来宾'])
print (repr([u'焦来宾']))

print (u'\u7126') #焦

str = '1'
print (ord(str))
print (hex(ord(str)))

#数据计算
print (abs(-0.07))

#如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
#print (cmp(1,-2))

#返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print (round(4.3))
print (round(4.3333, 6))

print (isinstance(round(4.3333), int))
print (isinstance(round(4.3333, 6), float))

