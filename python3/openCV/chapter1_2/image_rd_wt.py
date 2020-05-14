import numpy
import cv2
import os


# 创建一个像素图像
#img = numpy.zeros((3,3), dtype=numpy.uint8)
#print(img)


# 利用cv2.cvtColor将图像转换成BGR格式
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#print(img)


# 图像读取
#img = cv2.imread('D:/test/computer16px.png') # 默认是BGR格式  与  RGB格式相同 字节顺序相反 16*16*3
#img = cv2.imread('D:/test/computer16px.png', cv2.IMREAD_ANYCOLOR)
#img = cv2.imread('D:/test/computer16px.png', cv2.IMREAD_COLOR)

#img = cv2.imread('D:/test/computer16px.png', cv2.IMREAD_GRAYSCALE)  # 灰度图像 16*16
#img = cv2.imread('D:/test/computer16px.png', cv2.IMREAD_ANYDEPTH)  # 灰度图像 16*16

#img = cv2.imread('D:/test/computer16px.png', cv2.IMREAD_LOAD_GDAL) # 16*16*4

#print(img)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(img)
#print(img.shape)

# 写图像 产生一个随机另存为jpg格式
array_1 = bytearray(os.urandom(360000))
array_2 = numpy.array(array_1)
img = array_2.reshape(300,400,3)    # 灰度图像

cv2.imshow("test",img )
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('D:/test/random1.jpg', img)

#img = array_2.reshape(100,400,3)  # 彩色图像
#cv2.imwrite('D:/test/random2.jpg', img)
