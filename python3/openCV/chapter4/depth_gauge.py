# grabcut图像分割 提取图中图像并消除背景

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:/test/Grabcut.png')
mask = np.zeros(img.shape[:2], np.uint8)  # 二维掩模

bgdModel = np.zeros((1,65), np.float64)  # 创建前景和背景模型
fgdModel = np.zeros((1,65), np.float64)

rect = (100, 50, 500, 400)  # 用标识出想要隔离的对象的矩形来初始化算法
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')  # 将0-3值的掩模 二值化
img = img*mask2[:,:,np.newaxis]  #过滤掉0值像素

plt.subplot(121), plt.imshow(img)
plt.title('grabcut'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread("D:/test/Grabcut.png"), cv2.COLOR_BGR2RGB))
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.show()
