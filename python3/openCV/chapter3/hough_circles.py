# hough变换是直线和醒转检测背后的理论基础
# 标准直线检测函数 HoughLines
# 概率直线检测函数 HoughLinesP 是优化版本

import cv2
import numpy as np

img = cv2.imread('D:/test/fanpai1.jpeg')

dev1 = img[850:970, 30:190]
dev2 = img[720:880, 820:1000]
dev3 = img[610:730, 1860:2000]

cv2.imshow("device1", dev1)
cv2.imshow("device2", dev2)
cv2.imshow("device3", dev3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mimg = cv2.medianBlur(gray, 5)
cimg = cv2.cvtColor(mimg,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(mimg,cv2.HOUGH_GRADIENT,1,100,
                            param1=100,param2=30,minRadius=10,maxRadius=60)

print(circles)
#circles = np.uint16(np.around(circles))

if circles is not None:
    print(circles)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)
        # draw the center of the circle
        # cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

# cv2.imwrite("planets_circles.jpg", mimg)
cv2.imshow("HoughCirlces", img)
cv2.waitKey()
cv2.destroyAllWindows()
