import numpy as np
import cv2

# SURF 的计算速度比 SIFT要快很多 受到专利的保护，两者都在xfeatures2d模块中

img = cv2.imread("D:/test/waleize.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Hessian阈值8000 阈值越高能识别的特征就越少
sift = cv2.xfeatures2d.SURF_create(8000.0)
keypoints, descriptor = sift.detectAndCompute(gray,None)  # 返回关键点信息和描述符

# 为每个特征绘制圆圈和方向
img = cv2.drawKeypoints(image=img, outImage=img, keypoints = keypoints,
                        flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color = (51, 163, 236))

cv2.imshow('sift_keypoints', img)
cv2.waitKey()
cv2.destroyAllWindows()


