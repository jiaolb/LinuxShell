# 高通滤波器
# 1.利用卷积的方式实现高通滤波功能
# 2.利用高斯模糊的低通滤波功能进行滤波 然后与原始图像计算差值

import cv2
import numpy as np
from scipy import ndimage


kernel_3x3 = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

img = cv2.imread("D:/test/test_color.png", cv2.IMREAD_GRAYSCALE)

# ndimage的convolve函数可以用来求卷积 numpy中的卷及计算只限于一维数组，需要转换
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

# 高斯模糊
blurred = cv2.GaussianBlur(img, (17,17), 0)
g_hpf = img - blurred

cv2.imshow("original", img)
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("blurred", blurred)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()

