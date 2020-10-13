"""
    利用 opencv 保存视频
    author: czjing
    source: https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
"""

import numpy as np
import cv2

# 创建一个video capture的实例
capture = cv2.VideoCapture(0)

# Define the codec
# In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2.
# XVID is more preferable.
# MJPG results in high size video.
# X264 gives very small size video
fourcc = cv2.VideoWriter_fourcc(*'XVID')            # DIVX, XVID, MJPG, X264, WMV1, WMV2.

# Create a VideoWriter object
output_video = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while capture.isOpened():
    hasFrame, frame = capture.read()

    if not hasFrame:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 图像上下翻转
    # frame = cv2.flip(frame, 0)

    # 保存视频
    output_video.write(frame)

    # 预览视频
    cv2.imshow('frame', frame)

    # 退出视频
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
capture.release()
output_video.release()
cv2.destroyAllWindows()