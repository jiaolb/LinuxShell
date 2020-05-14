# 检测故指的闪灯和翻牌

import cv2
import numpy as np
from scipy import ndimage

# 抓取或者加载图片
img_ori = cv2.imread('D:/test/device/yuanshi.jpeg')
img_fp = cv2.imread('D:/test/device/fanpai1.jpeg')
img_fpld = cv2.imread('D:/test/device/liangdneg2.jpeg')

# 标定目标区域
dev1_ori = img_ori[590:710, 30:190]
dev2_ori = img_ori[700:860, 900:1080]
dev3_ori = img_ori[850:970, 1860:2000]

dev1_fp = img_fp[850:970, 30:190]
dev2_fp = img_fp[720:880, 820:1000]
dev3_fp = img_fp[610:730, 1860:2000]

dev1_fpld = img_fpld[850:970, 30:190]
dev2_fpld = img_fpld[720:880, 820:1000]
dev3_fpld = img_fpld[610:730, 1860:2000]

def ShowImageRect(dev):
    if dev == 0:
        cv2.imshow("dev1",   dev1_ori)
        cv2.imshow("dev1fp", dev1_fp)
        cv2.imshow("dev1ld", dev1_fpld)
        print(dev1_ori.shape)
    elif dev == 1:
        cv2.imshow("dev2",   dev2_ori)
        cv2.imshow("dev2fp", dev2_fp)
        cv2.imshow("dev2ld", dev2_fpld)
        print(dev2_ori.shape)
    elif dev == 2:
        cv2.imshow("dev3",   dev3_ori)
        cv2.imshow("dev3fp", dev3_fp)
        cv2.imshow("dev3ld", dev3_fpld)
        print(dev3_ori.shape)


# 亮灯检测方法1 - 亮度比对
'''
def filter_brightness_low(src_img, dst_img, bsize, limit):
    gray = cv2.cvtColor(src_img.copy(), cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, bsize, 0)
    ret, thresh1 = cv2.threshold(blur, limit, 255, 0)

    gray = cv2.cvtColor(dst_img.copy(), cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, bsize, 0)
    ret, thresh2 = cv2.threshold(blur, limit, 255, 0)

    img, count = thresh2-thresh1, 0
    for i in img[img >= 255]:
        count += 1
    print('high bright count:{:d}'.format(count))
    return img, count

def filter_brightnesslow(src_img, bsize, limit):
    gray = cv2.cvtColor(src_img.copy(), cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, bsize, 0)
    ret, thresh = cv2.threshold(blur, limit, 255, 0)
    count = 0
    for i in thresh[thresh >= 255]:
        count += 1
    print('high bright count:{:d}'.format(count))
    return thresh, count

ShowImageRect(1)

img1, n = filter_brightnesslow(dev2_ori, (17,17), 150)
cv2.imshow("dev201", img1)

img2, n = filter_brightnesslow(dev2_fp, (17,17), 150)
cv2.imshow("dev202", img2)

img3, n = filter_brightnesslow(dev2_fpld, (17,17), 150)
cv2.imshow("dev203", img3)
'''

# 翻牌检测方法1  过滤其他颜色
def filter_without_red(src_img, min_val, max_val=255):
    point = 0
    image = np.zeros(src_img.shape, np.uint8)
    for i in range(src_img.shape[0]):
        for j in range(src_img.shape[1]):
            if src_img[i][j][2] > min_val and src_img[i][j][2] <= max_val:
                if src_img[i][j][0] < min_val and src_img[i][j][1] < min_val:
                    image[i][j][2] = 255
                    point += 1
    print('red point count:{:d}'.format(point))
    return image,point

ShowImageRect(0)

img1,n = filter_without_red(dev1_ori, 65)
cv2.imshow("dev201", img1)

img2,n = filter_without_red(dev1_fp, 65)
cv2.imshow("dev202", img2)

img3,n = filter_without_red(dev1_fpld, 65)
cv2.imshow("dev203", img3)



'''
gray = cv2.cvtColor(dev1, cv2.COLOR_BGR2GRAY)
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
        cv2.circle(dev1, (i[0], i[1]), i[2], (255, 0, 0), 2)
        # draw the center of the circle
        # cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

# cv2.imwrite("planets_circles.jpg", mimg)
cv2.imshow("HoughCirlces", dev1)
'''
cv2.waitKey()
cv2.destroyAllWindows()
