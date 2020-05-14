# hough变换是直线和醒转检测背后的理论基础
# 标准直线检测函数 HoughLines
# 概率直线检测函数 HoughLinesP 是优化版本

import cv2
import numpy as np

img = cv2.imread('D:/test/test_color.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,120)

minLineLength = 20  #  限制直线抓取的参数
maxLineGap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
  cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
