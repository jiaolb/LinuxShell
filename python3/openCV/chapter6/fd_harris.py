import numpy as np
import cv2

# 检测角点

img = cv2.imread("D:/test/chess.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 第三个参数表明角点检测的敏感度 取值3-31
dst = cv2.cornerHarris(gray, 5, 21, 0.04)

# 将检测的角点标记为红色
img[dst > 0.01 * dst.max() ] = [0, 0, 255]

cv2.imshow('corners', img)

cv2.waitKey()
cv2.destroyAllWindows()


