#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

myname = 'jiao laibin'

print (u'格式化与标题化:')
#格式化字符串
print ("{} {}".format("hello", myname))
#"标题化"的 string,就是说所有单词都是以大写开始
print (myname.title())

print ('\n', u'字符串最值与统计:')
#返回字符串 str 中最大的字母
print (max(myname))
print (min(myname))
#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print (myname.count('i'))
print (myname.count('i', 0, 3))

print ('\n', u'字符串对齐填充:')
#返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print (myname.center(20, '_'))
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print (myname.ljust(20, '_'))
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print (myname.rjust(20, '_'))
#返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
print (myname.zfill(20))

print ('\n', u'字符串查找:')
#检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
print (myname.startswith('bin'))
#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print (myname.endswith('bin'))
#检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print (myname.find('bin',0,10))
print (myname.index('bin'))
print (myname.rfind('bin'))#从右边开始查找
print (myname.rindex('bin'))

print ('\n', u'字符串内容比对:')
#如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print (myname.isalnum())
#如果 string 是标题化的(见 title())则返回 True，否则返回 False
print (myname.istitle())

print ('\n', u'大小写转换:')
#把字符串的第一个字符大写
print (myname.capitalize())
#转换 string 中所有大写字符为小写.
print (myname.swapcase())
#翻转 string 中的大小写
print (myname.lower())
#转换 string 中的小写字母为大写
print (myname.upper())

print ('\n', u'去除首尾空格符:')
#截掉 string 左边的空格
print ("  te st   ".lstrip())
#删除 string 右边的空格.
print ("  te st   ".rstrip())
#在 string 上执行 lstrip()和 rstrip()
print ("  te st   ".strip())

print ('\n', u'字符串替换:')
#以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
x = 'ss'.join(('1','2','3'))
print (x)
#把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
print (myname.replace('i','X', 1))
#把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
print (' ll'.expandtabs())
#maketrans() 方法用于创建字符映射的转换表
#intab = "lai"
#outtab = "bin"
#trantab = string.maketrans(intab, outtab)
##根据 str 给出的表(包含 256 个字符)转换 string 的字符,
#print (myname.translate(trantab))

print ('\n', u'字符串分片:')
#以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
print (myname.split('i'))
print (myname.split('i', 1))
print (myname.partition('i'))
print (myname.rpartition('i')) #从右边开始
#按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print ('jiao\rlai\nbin\r\n'.splitlines())





