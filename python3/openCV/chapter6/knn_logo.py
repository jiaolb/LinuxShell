import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("D:/test/csg_logo.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("D:/test/csg.png", cv2.IMREAD_GRAYSCALE)

# 创建ORB特征检测器和描述符
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.knnMatch(des1, des2, k=1)

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, img2, flags=2)
plt.imshow(img3)
plt.show()
