#轮廓检测 - 付诸实现计算多边形边界、形状逼近和计算感兴趣区域
#findContours函数可以找到二维图像数组的轮廓
#drawContours函数可以绘画三维图像数组的轮廓

import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)  # 生成一个二维矩阵 200*200像素
img[50:150, 50:150] = 200  # 二维矩阵中间区域置为空白 50-150行中的 50-150列置为白色

ret, thresh = cv2.threshold(img, 127, 255, 0)  # 图像二值化操作 >127置为255 反之置为0
print(img[50])
print(thresh[50])

#修改后的图像 图像的轮廓 层次 findContours （原图像 层次类型 轮廓逼近方法）
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # 格式转换为三位BGR
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)  #绘画一个绿色轮廓
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()