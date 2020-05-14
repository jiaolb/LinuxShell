# canny 边缘检测
# canny函数 opencv提供的一种边缘检测算法

# canny算法非常复杂，他先使用高斯滤波器对图像进行去噪、计算梯度、在边缘上使用非最大抑制（NMS）、在检测到
# 边缘上使用双阈值去除假阳性，最后还会分析所有的边缘机器之间的连接，以保留真正的边缘并消除不明显的边缘。

import cv2

img = cv2.imread("D:/test/test_color.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("D:/test/canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("D:/test/canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
