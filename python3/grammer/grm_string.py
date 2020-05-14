#!/usr/bin/python
# -*- coding: UTF-8 -*-

myname = '''jiao 
laibin'''

def myprint(title, content):
    print (title, ' ', content)

#访问字符串
print (u'全名', ' ', myname)
myprint(u'姓氏', myname[0:4])

#更新字符串
myprint(u'原名', myname[0:5] + 'hongjin')

#输入一个响铃 '\a'
print ('\a')

#退格
print ('test \bstring')

#纵向制表符
print ('test \v','string')

#横向制表符
print ('test\t','string')

#原始字符串
print ('test\n','string')

#字符串格式化
print ('MyName is %s' % myname)

#小数点精度
print ('MyName is %.2f ' % 3.222222)

#在正数前面显示加号( + )
print ('%+d'% 3.22)


