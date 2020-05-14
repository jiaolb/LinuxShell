import numpy as np
import cv2

# 关键点一般具有如下属性定义
'''
pt       - 点，关键点的坐标
size     - 特征的尺寸、直径
angle    - 特征的方向
response - 关键点的强度，可以理解为更好的特征
octave   - 特征所在的金字塔的层级
class_id - ID
'''

# 检测边缘

img = cv2.imread("D:/test/waleize.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray,None)  # 返回关键点信息和描述符

# 为每个特征绘制圆圈和方向
img = cv2.drawKeypoints(image=img, outImage=img, keypoints = keypoints,
                        flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color = (51, 163, 236))

cv2.imshow('sift_keypoints', img)
cv2.waitKey()
cv2.destroyAllWindows()


