#!/usr/bin/python
# -*- coding: UTF-8 -*-

#函数返回数字的绝对值
print (abs(-1))

#函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
print (divmod(10,3))

#方法对系列进行求和计算。
print (sum([1,2],4))

#函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False
print (all(''))
print (all(['',"1"]))

#any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。
print (any([0, '', False]))

#将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
seq = ['aa','bb','cc']
for i,j in enumerate(seq):
    print (i,seq[i])
    
#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print (eval('1+5'))

#判断一个对象是否是一个已知的类型
print (isinstance('str2', int))

#execfile可以用来执行一个文件。
#issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
#super() 函数用于调用下一个父类(超类)并返回该父类实例的方法
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
#callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
#

#getatt() 函数用于返回一个对象属性值。
#hasattr() 函数用于判断对象是否包含对应的属性。
#delattr 函数用于删除属性。
#setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在

#reduce() 函数会对参数序列中元素进行累积。
#locals() 函数会以字典类型返回当前位置的全部局部变量。
#memoryview() 函数返回给定参数的内存查看对象(Momory view)。

#reload() 用于重新载入之前载入的模块
#vars() 函数返回对象object的属性和属性值的字典对象。
#slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。


#map() 会根据提供的函数对指定序列做映射。
#zip() 解压与压缩

#compile() 函数将一个字符串编译为字节代码。







