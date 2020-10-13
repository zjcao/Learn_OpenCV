"""
    利用opencv读取读取摄像头
    author: czjing
    source: https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
"""

import numpy as np
import cv2

# 创建一个video capture的实例
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    hasFrame, frame = capture.read()

    # if frame is read correctly hasFrame is True
    if not hasFrame:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 显示内容
    # 将视频转换为灰度图像
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow("sensorViewer", frame)

    # 按q退出程序
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()

