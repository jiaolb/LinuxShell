# -*- coding:utf-8 -*-

# pip install numpy          依赖库，数值计算、矩阵计算
# pip install matplotlib     matlib
# pip install opencv-python  主
# pip install SciPy          科学计算库，依赖numpy
# pip install OpenNI         可选依赖库，支持深度摄像头
# pip install SensorKinect   可选依赖库，OpenNI插件，支持微软的Kinect摄像头



# 打开摄像头的一个例子
import cv2

#摄像头对象
cap=cv2.VideoCapture(0)
#显示
while(1):
    ret,frame = cap.read()
    cv2.imshow("capture",frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
