import numpy
import numpy.matlib
from matplotlib import pyplot as plt

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
#x = numpy.arange(0,  3  * numpy.pi,  0.1)
x = [10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0]

y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
print(x)
print(y_sin)
print(y_cos)
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
