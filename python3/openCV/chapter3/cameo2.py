# 加入滤波图像处理版本的cameo

import cv2
import openCV.chapter3.filters as filters
from openCV.chapter1_2.managers import WindowManager,CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            # filters.strokeEdges(frame, frame)
            # filters.SharpenFilter().apply(frame, frame)
            # filters.FindEdgesFilter().apply(frame, frame)
            # filters.BlurFilter().apply(frame, frame)
            filters.EmbossFilter().apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        ''' 空格键获取截图
            按tab键启动/停止截屏
            按ESC退出应用.'''
        if keycode == ord(' '):
            self._captureManager.writeImage('D:/test/camero.png')
        elif keycode == ord('\t'):
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('D:/test/camero.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    cameo = Cameo()
    cameo.run()