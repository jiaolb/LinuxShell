import numpy as np
import cv2

# ORB是一个更新的算法 用来取代SIFT和SURF，基于FAST关键点检测的技术和基于BRIEF描述符的技术相结合。

'''
1.FAST算法
在像素周围绘制圆，然后通过亮度检出圆心是否是角点。
2.BRIEF
这更像是一个描述符，一种快速的用于进行特征的匹配的方法。
3.暴力匹配
一种描述符匹配方法，称为暴力的原因是该算法不设计优化，第一个描述符的所有特征都用来和第二个描述符特征进行比较。
'''

img = cv2.imread("D:/test/waleize.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sift = cv2.ORB_create()
keypoints, descriptor = sift.detectAndCompute(gray,None)  # 返回关键点信息和描述符

# 为每个特征绘制圆圈和方向
img = cv2.drawKeypoints(image=img, outImage=img, keypoints = keypoints,
                        flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color = (51, 163, 236))

cv2.imshow('sift_keypoints', img)
cv2.waitKey()
cv2.destroyAllWindows()


