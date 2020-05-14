#!usr/bin/python
# -*- coding: UTF-8 -*-

print (u'算术运算符')
a,b,c = 21,10,0

print (u"1 - a + b 的值为：", a + b)
print (u"2 - a - b 的值为：", a - b)
print (u"3 - a * b 的值为：", a * b) 
print (u"4 - a / b 的值为：", a / b) 
print (u"5 - a % b 的值为：", a % b)
print (u"6 - a//b  的值为：", a//b )
a,b = 2,3
print (u"7 - 2**3 的值为：", a**b)

#######################################
print ('\r\n', u'比较运算符')
a,b,c = 21,10,0

print ('默认a=%d  b=%d c=%d' % (a,b,c))
 
if ( a == b ):
   print (u"1 - a 等于 b")
else:
   print (u"1 - a 不等于 b")
   
if ( a != b ):
   print (u"2 - a 不等于 b")
else:
   print (u"2 - a 等于 b")
 
#Python3取消了<>运算符号
#if ( a <> b ):
#   print (u"3 - a 不等于 b")
#else:
#   print (u"3 - a 等于 b")
if ( a < b ):
   print (u"4 - a 小于 b" )
else:
   print (u"4 - a 大于等于 b")
 
if ( a > b ):
   print (u"5 - a 大于 b")
else:
   print (u"5 - a 小于等于 b")
   
a,b = 5,20
if ( a <= b ):
   print (u"6 - a 小于等于 b")
else:
   print (u"6 - a 大于  b")
 
if ( b >= a ):
   print (u"7 - b 大于等于 a")
else:
   print (u"7 - b 小于 a")

#######################################
print ('\r\n', u'赋值运算符')
a,b,c = 21,10,0
c = a + b
print (u"1 - c 的值为：a + b = ", c)
c += a
print (u"2 - c += a 的值为：", c )
c *= a
print (u"3 - c *= a 的值为：", c )
c /= a 
print (u"4 - c /= a 的值为：", c )
c = 2
c %= a
print (u"5 - c = 2, c %= a 的值为：", c)
c **= a
print (u"6 - c **= a 的值为：", c)
c //= a
print (u"7 - c //= a 的值为：", c)

#######################################
print ('\r\n', u'位运算符')
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print (u"1 - c 的值为：", c)
 
c = a | b;        # 61 = 0011 1101 
print (u"2 - c 的值为：", c)
 
c = a ^ b;        # 49 = 0011 0001
print (u"3 - c 的值为：", c)
 
c = ~a;           # -61 = 1100 0011
print (u"4 - c 的值为：", c)
 
c = a << 2;       # 240 = 1111 0000
print (u"5 - c 的值为：", c)
 
c = a >> 2;       # 15 = 0000 1111
print (u"6 - c 的值为：", c)

#######################################
print ('\r\n', u'逻辑运算符')
a = 10
b = 20
 
if ( a and b ):
   print (u"1 - 变量 a 和 b 都为 true")
else:
   print (u"1 - 变量 a 和 b 有一个不为 true")
 
if ( a or b ):
   print (u"2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print (u"2 - 变量 a 和 b 都不为 true")
 
# 修改变量 a 的值
a = 0
if ( a and b ):
   print (u"3 - 变量 a 和 b 都为 true")
else:
   print (u"3 - 变量 a 和 b 有一个不为 true")
 
if ( a or b ):
   print (u"4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print (u"4 - 变量 a 和 b 都不为 true")
 
if not( a and b ):
   print (u"5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print (u"5 - 变量 a 和 b 都为 true")

#######################################
print ('\r\n', u'成员运算符')
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print (u"1 - 变量 a 在给定的列表中 list 中")
else:
   print (u"1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print (u"2 - 变量 b 不在给定的列表中 list 中")
else:
   print (u"2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
   print (u"3 - 变量 a 在给定的列表中 list 中")
else:
   print (u"3 - 变量 a 不在给定的列表中 list 中")

#######################################
print ('\r\n', u'身份运算符')
a = 20
b = 20

if ( a is b ):
   print (u"1 - a 和 b 有相同的标识")
else:
   print (u"1 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print (u"2 - a 和 b 没有相同的标识")
else:
   print (u"2 - a 和 b 有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print (u"3 - a 和 b 有相同的标识")
else:
   print (u"3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print (u"4 - a 和 b 没有相同的标识")
else:
   print (u"4 - a 和 b 有相同的标识")
