import cv2

# 做一个视频转换器 把mp4格式的文件转换为avi格式

video = cv2.VideoCapture('D:/test/child.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(fps, size)

videoWt = cv2.VideoWriter('D:/test/child2.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
success,frame = video.read()
while success:
    videoWt.write(frame)
    success, frame = video.read()

# 编解码器常用选项
'''
# 1.未压缩的YUV颜色编码，是4:2:0色度子采样，这种编码有很好的兼容性，但会产生较大文件，文件扩展名.avi。
cv2.VideoWriter_fourcc('I', '4', '2', '0')
# 2.MPEG-1编码类型，文件扩展名.avi。
cv2.VideoWriter_fourcc('P', 'I', 'M', '1')
# 3.MPEG-4编码类型，如果希望得到的视频大小为平均值，采用此选项，文件扩展名.avi。
cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# 4.Ogg Vorbis，文件扩展名.ogv。
cv2.VideoWriter_fourcc('T', 'H', 'E', 'O')
# 5.Flash视频，文件扩展名.flv。
cv2.VideoWriter_fourcc('F', 'L', 'V', '1')
'''
