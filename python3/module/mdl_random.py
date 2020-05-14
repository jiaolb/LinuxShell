#!usr/bin/python
# _*_ coding: UTF-8 _*_

import random as r

#从序列的元素中随机挑选一个元素
print (u'随机数字', r.choice(range(10)))

#从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
print (u'随机偶数', r.randrange(0,100,2))

#随机生成下一个实数，它在[0,1)范围内
print (r.random())

#改变随机数生成器的种子seed
r.seed( 10 )
print ("Random number : ", r.random())
print ("Random number : ", r.random())
print ("Random number : ", r.random())

#将序列的所有元素随机排序
x = list(range(10))
r.shuffle(x)
print (x)

#随机生成下一个实数，它在[x,y]范围内。
print (r.uniform(1,2))



