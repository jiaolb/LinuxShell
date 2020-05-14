# 深入理解for循环 和 迭代

# 1 Python中的for循环与其他语言不同 Python 的 for 循环不使用索引 实际上是一个迭代
numbers = [1, 2, 3, 5, 7]
squares = (n**2 for n in numbers)  # 第一次循环
#print(tuple(squares))
#print(sum(squares))  # 第二次循环 迭代已耗尽

print(9 in squares)  # 第一次循环
print(9 in squares)  # 第二次循环 迭代已耗尽

# 2 迭代器驱动 for 循环
numbers = [1, 2, 3]
my_iterator = iter(numbers)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))  # 再次使用 引发StopIteration错误

# 3 yield 允许在调用 next 函数之间暂停生成器函数。yield 语句是将生成器函数与常规函数分离的东西。
numbers = [1, 2, 3, 5, 7]
def square_all(numbers):
    for n in numbers:
        yield n**2

squares = square_all(numbers)  # 表达方式1
print(next(squares))

# squares = (n**2 for n in numbers) # 与表达方式1相同的效果

# 4 打破循环
from itertools import islice

first_ten_lines = islice(numbers, 3)
for line in first_ten_lines:
    print(line)

