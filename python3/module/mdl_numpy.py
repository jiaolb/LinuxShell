import numpy
import numpy.matlib
from matplotlib import pyplot as plt

# 数组的算数和逻辑运算。
# 傅立叶变换和用于图形操作的例程。
# 与线性代数有关的操作, NumPy 拥有线性代数和随机数生成的内置函数。

# NumPy 中定义的最重要的对象是称为 ndarray 的 N 维数组类型。 它描述相同类型的元素集合。
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# 1.object 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列。
# 2.dtype 数组的所需数据类型，可选。
# 3.copy 可选，默认为true，对象是否被复制。
# 4.order C（按行）、F（按列）或A（任意，默认）。
# 5.subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
# 6.ndimin 指定返回数组的最小维数。
print("1.array() ************************************************")

x = [1, 2, 3, 4]
y = [11, 12, 13, 14]
z = [21, 22, 23, 264]

a = numpy.array([x, y, z], dtype=numpy.uint8)  # 264越限了
print(a)
print(a[2][3])

#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
a = numpy.array(z, dtype='i2')
print(a)

print("2.dtype() ************************************************")
dt = numpy.dtype([('age',numpy.int8)])
a = numpy.array([(10,),(20,),(257,)], dtype = dt)
print(a)
print(a['age'])

student = numpy.dtype([('name', 'U20'), ('age', 'i1'), ('count', 'f4')])
a = numpy.array([(u'张三',  21,  50),(u'李四',  18,  75)], dtype=student)
print(a)

print("3.Array prop ************************************************")
a = numpy.arange(1,20,2)
print(a)
print(a.shape)  # 一个包含数组维度的元组，它也可以用于调整数组大小
print(a.ndim)   # 维度
print(a.itemsize)  # 数组中每个元素的字节单位长度
a.shape = (2,5)   # b = a.reshape(1,12)
print(a)
# print(a.flags)

print("3.Array 创建例程 ************************************************")
# empty 创建指定形状和dtype的未初始化数组
a = numpy.empty([3,2], dtype =  int)
print(a)

# 返回特定大小，以 0 填充的新数组
a = numpy.zeros(10, dtype=numpy.uint16)  # 默认为float类型
print(a)

# 返回特定大小，以 1 填充的新数组
a = numpy.ones([2,5], dtype=numpy.uint16)# 默认为float类型
print(a)

print("4.Array 来自现有数据的数组 ************************************************")
# 简化版 asarray(a, dtype = None, order = None)
a = numpy.asarray([1,2,3,4])
print(a)

# 将缓冲区解释为一维数组 frombuffer(buffer, dtype = float, count = -1, offset = 0)
# s = "hello world"
# a = numpy.frombuffer(s, dtype='S1')
# print(a)

# 从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组
list = range(5)
a = numpy.fromiter(iter(list), dtype=float)
print(a)

# 类似于arange()函数。 在此函数中，指定了范围之间的均匀间隔数量，而不是步长
x = numpy.linspace(10,20,5)
print(x)

# 返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字
a = numpy.logspace(1.0,  2.0, num =  10)
print(a)

print("5. 切片和索引 ************************************************")
a = numpy.arange(10)
b = a[2:7:2]
print(b)
s = slice(2,7,2)
print(a[s])

a = numpy.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[...,1])   # 第2列
print(a[1,...])   # 第2行
print(a[...,1:])  # 第2列以后
print(a[1:4,1:3])

y = a[[0, 1, 2],  [0, 1, 0]]
print(y)  # 依次选取0,1,2行的第0,1,0列数据

print(a[a >= 5])  # 索引出不小于5的数据

a = numpy.array([numpy.nan, 1, 2, numpy.nan, 3, 4, 5])  # 过滤NaN
print(a[~numpy.isnan(a)])

print("6. 广播 算术运算期间处理不同形状的数组的能力 *****************************")
a = numpy.array([1,2,3,4])
b = numpy.array([10,20,30,40])
print(a * b)

a = numpy.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = numpy.array([1.0,2.0,3.0])
print(a + b)

print("7. 数组上的迭代 ************************************************")
a = numpy.arange(0,60,5)
a = a.reshape(3,4)
for x in numpy.nditer(a):
    print(x, end=' ')
print()

# 数组的转置 如果相同元素使用 F 风格顺序存储，则迭代器选择以更有效的方式对数组进行迭代。
b = a.T
print(b)
for x in numpy.nditer(b):
    print(x, end=' ')
print()

for x in numpy.nditer(b, order='C'):
    print(x, end=' ')
print()

for x in numpy.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print(b)

# 该函数返回数组上的一维迭代器
print(b.flat[5])

# 该函数返回折叠为一维的数组副本
print(b.flatten())

# 这个函数返回展开的一维数组，并且按需生成副本
print(b.ravel(order = 'F'))

print("7. 数组操作 ************************************************")
# 翻转给定数组的维度
print(numpy.transpose(b))

# 该函数向后滚动特定的轴，直到一个特定位置
print(numpy.rollaxis(numpy.transpose(b),1))

# 该函数交换数组的两个轴
print(numpy.swapaxes(numpy.transpose(b),1,0))

# 返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
x = numpy.array([[1], [2], [3]])
y = numpy.array([4, 5, 6])
b = numpy.broadcast(x, y)
print(b.shape)
c = numpy.empty(b.shape)
c.flat = [u + v for (u,v) in b]
print(c)

# 此函数将数组广播到新形状
a = numpy.arange(4).reshape(1,4)
print(numpy.broadcast_to(a,(4,4)))

# 函数通过在指定位置插入新的轴来扩展数组形状
x = numpy.array(([1,2],[3,4]))
y = numpy.expand_dims(x, axis = 0)
print(y)

# 函数从给定数组的形状中删除一维条目
x = numpy.arange(9).reshape(1,3,3)
y = numpy.squeeze(x)
print(x)
print(y)

# 数组连接
# concatenate 沿着现存的轴连接数据序列
# stack 沿着新轴连接数组序列
# hstack 水平堆叠序列中的数组（列方向）
# vstack 竖直堆叠序列中的数组（行方向）

# 数组分割
# split 将一个数组分割为多个子数组
# hsplit 将一个数组水平分割为多个子数组（按列）
# vsplit 将一个数组竖直分割为多个子数组（按行）

# 添加/删除元素
# resize 返回指定形状的新数组
# append 将值添加到数组末尾
# insert 沿指定轴将值插入到指定下标之前
# delete 返回删掉某个轴的子数组的新数组
# unique 寻找数组内的唯一元素

print("8. 位操作 ************************************************")
# bitwise_and 对数组元素执行位与操作
# bitwise_or 对数组元素执行位或操作
# invert 计算位非
# left_shift 向左移动二进制表示的位
# right_shift 向右移动二进制表示的位

print("9. 字符串函数 ************************************************")
# add() 返回两个str或Unicode数组的逐个字符串连接
# multiply() 返回按元素多重连接后的字符串
# center() 返回给定字符串的副本，其中元素位于特定字符串的中央
# capitalize() 返回给定字符串的副本，其中只有第一个字符串大写
# title() 返回字符串或 Unicode 的按元素标题转换版本
# lower() 返回一个数组，其元素转换为小写
# upper() 返回一个数组，其元素转换为大写
# split() 返回字符串中的单词列表，并使用分隔符来分割
# splitlines() 返回元素中的行列表，以换行符分割
# strip()  返回数组副本，其中元素移除了开头或者结尾处的特定字符
# join()   返回一个字符串，它是序列中字符串的连接
# replace() 返回字符串的副本，其中所有子字符串的出现位置都被新字符串取代
# decode()  按元素调用str.decode
# encode()  按元素调用str.encode
print(numpy.char.add(['hello'],[' xyz']) )
print(numpy.char.add(['hello', 'hi'],[' abc', ' xyz']))
print(numpy.char.multiply('Hello ',3))

print(numpy.char.split ('hello how are you?'))
print(numpy.char.join([':','-'],['dmy','ymd']))

print("10. 算数函数 ************************************************")
# 三角函数
# sin(a*np.pi/180)  角度a正弦值
# cos(a*np.pi/180)  角度a余弦值
# tan(a*np.pi/180)  角度a正切值
a = numpy.array([0,30,45,60,90])
sin = numpy.sin(a*numpy.pi/180)
inv = numpy.arcsin(sin)
print(sin)
print(inv)

# 舍入函数
a = numpy.array([1.0, 5.55, 123, 0.567, 25.532])
print(numpy.around(a))
print(numpy.around(a, decimals=1))
print(numpy.around(a, decimals=-1))

# 返回不大于输入参数的最大整数
a = numpy.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(numpy.floor(a))  # 向下舍入
print(numpy.ceil(a))   # 向上舍入

# 算数运算
a = numpy.arange(9, dtype = numpy.float_).reshape(3,3)
b = numpy.array([10,10,10])
print(numpy.add(a,b))  # 两个数组相加
print(numpy.subtract(a,b))  # 两个数组相减
print(numpy.multiply(a,b))  # 两个数组相乘
print(numpy.divide(a,b))  # 两个数组相除

# 返回参数逐元素的倒数
a = numpy.array([0.25,  1.33,  1,  1,  100])
print(numpy.reciprocal(a))

# 将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
a = numpy.array([10,100,1000])
print(numpy.power(a,2))

# 此函数返回输入数组中相应元素的除法余数。 函数numpy.remainder()也产生相同的结果
a = numpy.array([10,20,30])
b = numpy.array([3,5,7])
print(numpy.mod(a,b))
print(numpy.remainder(a,b))

# 以下函数用于对含有复数的数组执行操作。
# numpy.real() 返回复数类型参数的实部。
# numpy.imag() 返回复数类型参数的虚部。
# numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
# numpy.angle() 返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。

print("11. 统计函数 ************************************************")
# numpy.amin() 和 numpy.amax() 从给定数组中的元素沿指定轴返回最小值和最大值。
a = numpy.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(numpy.amin(a, 1))
print(numpy.amin(a, 0))
print(numpy.amax(a))
print(numpy.amax(a, axis=0))

# numpy.ptp()函数返回沿轴的值的范围（最大值 - 最小值）
a = numpy.array([[3,7,5],[8,4,3],[2,4,9]])
print(numpy.ptp(a))
print(numpy.ptp(a, axis =  1))
print(numpy.ptp(a, axis =  0))

# 百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
a = numpy.array([[30,40,70],[80,20,10],[50,90,60]])
print(numpy.percentile(a,50))
print(numpy.percentile(a,50, axis =  1))
print(numpy.percentile(a,50, axis =  0))

# numpy.median() 中值定义为将数据样本的上半部分与下半部分分开的值。
# numpy.mean() 算术平均值是沿轴的元素的总和除以元素的数量。
# numpy.average() 加权平均值是由每个分量乘以反映其重要性的因子得到的平均值。
# numpy.std() 标准差是与均值的偏差的平方的平均值的平方根。 std = sqrt(mean((x - x.mean())**2))
# numpy.var() 方差是偏差的平方的平均值，即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根。

print("12. 排序、搜索和计数函数 ************************************************")
# 种类	                速度	最坏情况	  工作空间	稳定性
# 'quicksort'（快速排序）	1	O(n^2)	     0	    否
# 'mergesort'（归并排序）	2	O(n*log(n))	~n/2	是
# 'heapsort'（堆排序）	3	O(n*log(n))	 0	    否

# numpy.sort()
# numpy.argsort() 函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。
# numpy.lexsort() 函数使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。
# numpy.argmax() 和 numpy.argmin() 这两个函数分别沿给定轴返回最大和最小元素的索引。
# numpy.nonzero()函数返回输入数组中非零元素的索引。
# numpy.where()函数返回输入数组中满足给定条件的元素的索引。
# numpy.extract()函数返回满足任何条件的元素。

dt = numpy.dtype([('name',  'S10'),('age',  int)])
a = numpy.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print(numpy.sort(a, order =  'name'))

print("13. 字节交换 ************************************************")
# numpy.ndarray.byteswap()函数在两个表示：大端和小端之间切换。
a = numpy.array([1,  256,  8755], dtype = numpy.int16)
print(a.byteswap(True))

print("14. 副本和视图 ************************************************")
# NumPy 拥有ndarray.view()方法，它是一个新的数组对象，并可查看原始数组的相同数据。 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。
# ndarray.copy()函数创建一个深层副本。 它是数组及其数据的完整副本，不与原始数组共享。

print("15. 矩阵库 ************************************************")
# NumPy 包包含一个 Matrix库numpy.matlib
# numpy.matlib.empty()函数返回一个新的矩阵，而不初始化元素。
# numpy.matlib.zeros()此函数返回以零填充的矩阵。
# numpy.matlib.ones() 此函数返回以一填充的矩阵。
# numpy.matlib.eye()这个函数返回一个矩阵，对角线元素为 1，其他位置为零。
# numpy.matlib.identity()函数返回给定大小的单位矩阵。单位矩阵是主对角线元素都为 1 的方阵。
# numpy.matlib.rand()`函数返回给定大小的填充随机值的矩阵。
print(numpy.matlib.identity(5, dtype =  float))

print("16. 线性代数 ************************************************")
# NumPy 包包含numpy.linalg模块，提供线性代数所需的所有功能
# 1.dot 两个数组的点积
# 2.vdot 两个向量的点积
# 3.inner 两个数组的内积
# 4.matmul 两个数组的矩阵积
# 5.determinant 数组的行列式
# 6.solve 求解线性矩阵方程
# 7.inv 寻找矩阵的乘法逆矩阵

print("17. Matplotlib ************************************************")
'''x = numpy.arange(1,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()

# 计算正弦曲线上点的 x 和 y 坐标
x = numpy.arange(0,  3  * numpy.pi,  0.1)
y = numpy.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()'''

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = numpy.arange(0,  3  * numpy.pi,  0.1)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()
