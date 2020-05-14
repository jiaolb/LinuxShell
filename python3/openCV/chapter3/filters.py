import cv2
import numpy
import openCV.chapter3.utils as utils


'''
常用的边缘检测滤波函数有 Laplacian()、Sobel()、Scharr()。思想都是将非边缘区域转换黑色，或者将边缘区域为白色或者其他饱和颜色。
为了有效地去除噪声，一般先将图片进行模糊处理，再进行边缘检测滤波。
常用的模糊处理函数有blur()算术平均、medianBlur()中位数模糊、GaussianBlur()高斯模糊。
'''
def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    '''边缘检测函数 输出黑色边缘和白色背景的彩色图像。'''
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)  # 把图像转换成灰度色彩空间
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)  # 检测出边缘
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)  # 将其值归一化 在0-1之间 然后乘以原图像使边缘变黑
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)

# 测试strokeEdges()
# img = cv2.imread("D:/test/test_color.png")
# cv2.imshow("original", img)

# blurredSrc = cv2.medianBlur(img, 7)  # 直接输出
# graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
# cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=5)
# cv2.imshow("stroke", graySrc)

# strokeEdges(img, img)  # 调用函数
# cv2.imshow("stroke", img)
# cv2.waitKey()
# cv2.destroyAllWindows()


'''
卷积矩阵是一个二维数组，有奇数行、奇数列，中心的元素对应于感兴趣的像素，其他的元素对英语这个像素周期的临近像素，
    每个元素都有一个整数或浮点数的值，这些值就是应用在像素值上的权重。
    新像素值 = 当前像素值*中心权重 - 剩余临近像素值*对应的临近像素权重
'''
class VConvolutionFilter(object):
    def __init__(self, kernel):
        super(VConvolutionFilter, self).__init__()
        self._kernel = kernel

    def apply(self, src, dst):
        '''filter2D函数利用客户指定的任意核或卷积矩阵计算卷积，第二个参数为矩阵目标图像每个数据元素的位深度，如cv2.CV_8U代表8位数据。
           如果为负值，代表目标图像和原图像的位深度是一致的。'''
        cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
    '''锐化滤波器'''
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
        super(SharpenFilter, self).__init__(kernel)

class FindEdgesFilter(VConvolutionFilter):
    '''边缘检测滤波器'''
    def __init__(self):
        '''权重之和为1，这样不改变图像的亮度，如果权重值和为0， 就会得到一个边缘检测的核'''
        kernel = numpy.array([[-1, -1, -1],
                              [-1,  8, -1],
                              [-1, -1, -1]])
        super(FindEdgesFilter, self).__init__(kernel)

class BlurFilter(VConvolutionFilter):
    '''模糊滤波器'''
    def __init__(self):
        '''权重之和为1，这样不改变图像的亮度，如果权重值和为0， 就会得到一个边缘检测的核。'''
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04]])
        super(BlurFilter, self).__init__(kernel)

class EmbossFilter(VConvolutionFilter):
    '''浮雕滤波器，与便边缘检测、锐化、以及模糊滤波器不同的是核不是对称的。'''
    def __init__(self):
        kernel = numpy.array([[-2, -1, 0],
                              [-1,  1, 1],
                              [ 0,  1, 2]])
        super(EmbossFilter, self).__init__(kernel)

# 测试滤波器
# img = cv2.imread("D:/test/test_color.png", cv2.IMREAD_GRAYSCALE)
# img1 = img.copy()
# img2 = img.copy()
# img3 = img.copy()
# img4 = img.copy()
#
# SharpenFilter().apply(img1, img1)
# FindEdgesFilter().apply(img2, img2)
# BlurFilter().apply(img3, img3)
# EmbossFilter().apply(img4, img4)
#
# cv2.imshow('orginal', img)
# cv2.imshow("Sharpen", img1)
# cv2.imshow("Edges", img2)
# cv2.imshow("Blur", img3)
# cv2.imshow("Emboss", img4)
# cv2.waitKey()
# cv2.destroyAllWindows()




