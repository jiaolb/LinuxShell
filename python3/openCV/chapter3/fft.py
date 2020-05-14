# 傅里叶变换 显示图像的采集、滤波和复原

import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('D:/test/test_color.png', 0)
f = np.fft.fft2(img)  # 进行二维离散傅里叶变换
fshift = np.fft.fftshift(f)  # 正方向移位 将DC分量移位到频谱中心
magnitude_spectrum = 20 * np.log(np.abs(fshift))  # 幅度谱

row, cols = img.shape
crow, ccol = row / 2, cols / 2
crow = int(crow)
ccol = int(ccol)
fshift[crow - 30: crow+30, ccol - 30: ccol + 30] = 0  #高通滤波

f_ishift = np.fft.ifftshift(fshift)  # 负方向移位
img_back = np.fft.ifft2(f_ishift)   # 反傅里叶变换  复原图像
img_back = np.abs(img_back)

plot.subplot(221), plot.imshow(img, cmap = "gray")
plot.title("Input"), plot.xticks([]), plot.yticks([])

plot.subplot(222), plot.imshow(magnitude_spectrum, cmap = "gray")
plot.title('magnitude_spectrum'), plot.xticks([]), plot.yticks([])

plot.subplot(223), plot.imshow(img_back, cmap = "gray")
plot.title("Input in JET"), plot.xticks([]), plot.yticks([])
plot.show()