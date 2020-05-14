import cv2

# 显示一个图像
img1 = cv2.imread('H:/SNAP.PPM')
img2 = cv2.imread('H:/COPY.PPM')
cv2.imshow('window_title1', img1)
cv2.imshow('window_title2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# 显示一个摄像头图像
# 任意窗口下都可以通过waitKey()函数来获取键盘输入，通过setMouseCallback()函数来获取鼠标输入
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:  # 任何按键按下并松开
        clicked = True

cameraCap = cv2.VideoCapture(0)
cv2.namedWindow('Hello World')
cv2.setMouseCallback('Hello World', onMouse)

# waitKey()参数为等待键盘出发时间 单位1ms，默认返回-1，有按键按下时返回相应的ASCII码
success,frame = cameraCap.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Hello World', frame)
    success, frame = cameraCap.read()

cv2.destroyWindow('Hello World')
cameraCap.release()
'''
# 鼠标事件列表
'''
cv2.EVENT_MOUSEMOVE
cv2.EVENT_LBUTTONUP      # 松开
cv2.EVENT_LBUTTONDOWN    # 按下
cv2.EVENT_LBUTTONDBLCLK  # 双击
cv2.EVENT_RBUTTONUP
cv2.EVENT_RBUTTONDOWN
cv2.EVENT_RBUTTONDBLCLK
cv2.EVENT_MBUTTONUP
cv2.EVENT_MBUTTONDOWN
cv2.EVENT_MBUTTONDBLCLK
'''

# 可组合的鼠标事件列表
'''
cv2.EVENT_FLAG_ALTKEY    # Alt键
cv2.EVENT_FLAG_CTRLKEY   # Ctrl键
cv2.EVENT_FLAG_LBUTTON   # 鼠标左键
cv2.EVENT_FLAG_MBUTTON   # 鼠标中键
cv2.EVENT_FLAG_RBUTTON   # 鼠标右键
cv2.EVENT_FLAG_SHIFTKEY  # Shift键
'''
