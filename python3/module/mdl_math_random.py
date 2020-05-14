#!usr/bin/python
# -*- coding:UTF-8 -*-

import math
import random

sample_no = 0

def print_my(str, eval_str):
    global sample_no
    sample_no += 1
    print (sample_no,'.',str)
    print (eval_str,' = ',eval(eval_str))
    
print_my(u'返回数字的绝对值', 'abs(-1.22)')
print_my(u'返回数字的绝对值', 'math.fabs(-1.22)')

print('\r\n')
#print_my(u'数值比较，X<Y->-1，X=Y->0，X>Y->1', 'cmp(1,-1)')
print_my(u'数值比较，最大值', 'max([1,-1,24])')
print_my(u'数值比较，最小值', 'min([1,-1,24])')

print_my(u'返回数字的上入整数', 'math.ceil(-1.22)')
print ('math.ceil(3.55) = ', eval('math.ceil(3.55)'))
print_my(u'返回数字的下舍整数', 'math.floor(-1.22)')
print_my(u'返回数字的四舍五入数', 'round(-1.2244,3)')

print('\r\n')
print_my(u'返回e的幂', 'math.exp(1)')
print_my(u'幂计算', 'math.log(100,10)')
print_my(u'返回10为基数的幂', 'math.log10(10)')
print_my(u'返回平方根', 'math.sqrt(9)')
print_my(u'N次方运算', 'math.pow(2,4)')

print('\r\n')
print_my(u'返回整数与小数部分', 'math.modf(3.14)')


print('\r\n')
print_my(u'随机挑选', 'random.choice([1,2,3,4,5])')
print_my(u'指定范围内随机挑选', 'random.randrange(1,100,2)')
print_my(u'随机生成下一个实数，它在(0,1)', 'random.random()')
print_my(u'随机生成下一个实数，它在(x,y)', 'random.uniform(1,100)')
list = [1,2,3,4,5]
random.shuffle(list)
print (u'将序列的所有元素随机排序', list)

