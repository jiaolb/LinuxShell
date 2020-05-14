#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    u'所有员工的基类'
    empCount = 0
    __testSiYou = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print ("Total Person %d" % Employee.empCount)
        return Employee.empCount
        
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)
        
        
        
I = Employee("jiaolb", 9000)
SB = Employee("xiaolilin", 100)

print (SB.displayCount())
#print I.__testSiYou

print (getattr(I, 'name'))
print (hasattr(I, 'name'))
setattr(I, 'name', 'JiaoLB')
print (getattr(I, 'name'))

#delattr(I, 'name') 
#print getattr(I, 'name')

#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#__doc__ :类的文档字符串
#__name__: 类名
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print (I.__dict__)
print (I.__doc__)
print (Employee.__name__)
print (I.__module__)
print (Employee.__bases__)


