#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {}
me = {'name':'jiaolb', 'Age':27, 'shuxiang':'snake'}

#访问字典里的值
print (me['name'])
print (me)

#修改
me['shuxiang'] = u'蛇'
print (me['shuxiang'])

#删除
del me['shuxiang']
print (me)

#计算字典元素个数，即键的总数。
print (len(me))

#输出字典可打印的字符串表示。
print (str(me))

she = {'name':'fengyn', 'Age':25, 'shuxiang':'sheep'}
#返回一个字典的浅复制
dict1 = me.copy()
print (dict1)

#删除字典内所有元素
me.clear()
print (me)

#创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
keyseq = ('name', 'Age', 'shuxiang')
me = me.fromkeys(keyseq)
print (me)

#返回指定键的值，如果值不在字典中返回default值
print (me.get('name', 'jiaolb'))

#如果键在字典dict里返回true，否则返回false
print ('she' in me.keys())

#以列表返回可遍历的(键, 值) 元组数组
list1 = dict1.items()
print (list1)

print ()
print ()

#以列表返回一个字典所有的键
print (me.keys())

print (type(me.keys()))

#和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
me.setdefault('Name', 'jiaolb')
print (me)

#把字典dict2的键/值对更新到dict里
me.update(dict1)
print (me)

#以列表返回字典中的所有值
print ("Value : %s" %  dict1.values())


