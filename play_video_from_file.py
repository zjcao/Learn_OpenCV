"""
    利用opencv 播放视频
    author: czjing
    source: https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
"""

# 导入必须的包
import numpy as np
import cv2

# 视频路径
capture = cv2.VideoCapture(r'E:\Pycharm\handTracking\data\video\handGesture-5_3.avi')

while capture.isOpened():

    hasFrame, frame = capture.read()

    # if frame is read correctly ret is True
    if not hasFrame:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 转换为灰度
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示视频
    cv2.imshow('frame', frame)

    # 退出视频
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()