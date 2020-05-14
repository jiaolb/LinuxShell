# 实用分水岭法分割图像
# 把图像中低密度（变化很少）的区域想象成山谷 高密度（变化很多）的区域想象成山峰，向山谷中注入水直到不同的山谷中水开始汇聚，为了
# 组织不同山谷的水汇聚，可以设置一些栅栏，最后得到的栅栏就是图像分割。

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:/test/watershed.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 得到灰度图像
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 二值化

# 通过morphologyEx除噪音
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 图像膨胀操作 得到大部分都是背景的区域
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 反之，可以通过distanceTransdorm来获取确定的前景区域
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# 获取背景和前景的重合部分
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 根据重合部分和前景 设定栅栏
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown==255] = 0  # 如果对应的重合区域是白色的 那么置为栅栏

# 开始放水
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
plt.imshow(img)
plt.show()

