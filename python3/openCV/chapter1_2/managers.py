'''
案例中
使用manages.CaptureManager提取视频流，按照2——2,2——3中的使用方法；
使用manages.WindowManager抽象窗口和键盘
'''

import cv2
import numpy
import time


class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):
        super(CaptureManager, self).__init__()
        self.previewWindowManager = previewWindowManager  # 窗口管理类
        self.shouldMirrorPreview = shouldMirrorPreview
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        self._startTime = None
        self._framesElapsed = int(0)
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        '''捕获下一帧，如果有的话。'''
        #首先，检查任何以前的帧是否退出
        assert not self._enteredFrame, 'previous enterFrame() had no matching exitFrame()'

        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):
        '''画到窗口。 写入文件。 释放帧。'''
        # 检查是否有任何抓取的帧是可检索到的. 该获取器可以检索并缓存该帧
        if self.frame is None:
            self._enteredFrame = False
            return

        # 更新FPS估计和相关变量
        if self._framesElapsed == 0:
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed  # 计算时间内帧数量
        self._framesElapsed += 1

        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame = numpy.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            self._imageFilename = None

        self._writeVideoFrame()
        self._frame = None
        self._enteredFrame = False

    def writeImage(self, filename):
        self._imageFilename = filename

    def startWritingVideo(self, filename, encoding=cv2.VideoWriter_fourcc('I', '4', '2', '0')):
        self._videoFilename = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return

        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                if self._framesElapsed < 20:
                    return
                else:
                    fps = self._fpsEstimate
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)

        self._videoWriter.write(self._frame)


class WindowManager(object):
    def __init__(self, windowName, keypressCallback = None):
        super(WindowManager, self).__init__()
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            keycode &= 0xFF
            self.keypressCallback(keycode)


