import numpy
import cv2
import os

cameraCap = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cameraCap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWt = cv2.VideoWriter('D:/test/camera.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

success,frame = cameraCap.read()
numFramesRemaining = 10 * fps - 1  # 录像10秒
while success and numFramesRemaining > 0:
    videoWt.write(frame)
    success, frame = cameraCap.read()
    numFramesRemaining -= 1

cameraCap.release()

# 如果有一组摄像头 那么使用read是不合适的 如下实用
'''
cameraCap1 = cv2.VideoCapture(0)
cameraCap2 = cv2.VideoCapture(1)

success1 = cameraCap1.grab()
success2 = cameraCap1.grab()
if success1 and success2 :
    frame1 = cameraCap1.retrieve()
    frame2 = cameraCap1.retrieve()
'''
