#!/usr/bin/python
# -*- coding: UTF-8 -*-

GroupOne = [u'何刚', u'田星星', u'焦来宾', u'李龙龙']

#获取列表长度
print (u'原来用电组内人数:',len(GroupOne))

#访问列表值
print (u'组长是:',GroupOne[-4])

#列表截取
print (u'其他成员是:',GroupOne[1:] )

#删除列表元素
print (u'调走了成员:',GroupOne[0])
del GroupOne[0]

#列表追加
newPerson = u'王瑞'
print (u'新入成员:',newPerson)
GroupOne.append(newPerson)

#in 计算符
print (u'现在成员有:')
for x in GroupOne:
    print (x, end = " ")
print ()

#在列表末尾一次性追加另一个序列中的多个值
NewMember = [u'陈磊', u'姚丽丽']
print (u'新入两个成员:', NewMember)
GroupOne.extend(NewMember)
print (u'现在成员有:', GroupOne)

#元祖转换为列表
age = (30,28,29,29,27,27)
AgeList = list(age)
print (u'他们的年龄分别是:',AgeList)

#最大最小值计算符
print (u'最大年龄:',max(AgeList))
print (u'最小年龄:',min(AgeList))

#统计元素在列表中出现的次数
print (u'其中27岁的成员有%d个' % AgeList.count(27))

#列表比较
#print (cmp(GroupOne, AgeList))

#从列表中找出某个值第一个匹配项的索引位置
print (u'最大的成员是:', GroupOne[AgeList.index(max(AgeList))])

#将对象插入列表
NewPerson2 = u'郭飞'
print (u'又来了一个成员:', NewPerson2)
print (u'他的年龄是:', 26)
GroupOne.insert(-1, NewPerson2)
AgeList.insert(-1, 26)

def ShowMemberAndAge():
    print (u'成员和年龄分别是:')
    for x in GroupOne:
        print ('    ',x,AgeList[GroupOne.index(x)])

ShowMemberAndAge()

#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print (u'去掉女生:', GroupOne.pop(-1))
print (u'她的年龄是:',AgeList.pop())

#移除列表中某个值的第一个匹配项
print (u'去掉年龄最大的:',GroupOne[0])
GroupOne.remove(u'田星星')
AgeList.remove(30)

#反向列表中元素
AgeList.reverse()
print (u'年龄反向序',AgeList)

#对原列表进行排序
AgeList.sort()
print (u'年龄从小到大排序',AgeList)








