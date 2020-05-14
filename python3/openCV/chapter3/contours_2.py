#找出边界框 - 最小矩形区域 - 最小闭圆的轮廓

import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("D:/test/hummar.png", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for c in contours:
    # 找到边界框的坐标 坐标x,y 矩形的宽度w和高度h
    x, y, w, h = cv2.boundingRect(c)
    # 在（x，y） - (x + w， y + h)矩形上画出绿色线
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 找到最小矩形区域
    rect = cv2.minAreaRect(c)
    # 计算矩形的顶点
    box = cv2.boxPoints(rect)
    # box位浮点数 转换为整数
    box = np.int0(box)
    print(box)
    # 画蓝色框图 第二个参数变为一组点来表示多边形的轮廓
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    # 最小闭圆的检查 返回圆心坐标和半径 为浮点型数据
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    # 使用绿色线画圆
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)
    print('hello')

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
