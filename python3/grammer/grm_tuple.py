#!usr/bin/python
# _*_ coding: UTF-8 _*_

me = (u'jiaolb', 1989, 28, 'boy')

print (me)
#访问元组
print ('myname :', me[0])
print ('infomation:', me[1:])

#修改元组
she = ('fengyn', 1991, 26, 'gril')
print ('she', she)

us = me + she
print ("we are :", us)

#删除元组
del me
del she
print ('me:', me)
print ('she:', she)