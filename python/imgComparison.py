import cv2
import numpy as np
import os

print ("Press Ctrl * C to EXIT")

if os.path.exists('/dev/video0') == False:
  path = 'sudo modprobe bcm2835-v4l2 max_video_width=2592 max_video_height=1944'
  os.system (path)
  time.sleep(1)

width = 640
height = 480
cam = cv2.VideoCapture(0)
cam.set(3,width)
cam.set(4,height)
thres = 20 # set difference between pixel values between frames
trigger = (height * width) / 10   # 10% of pixels

winName = "Picture"
winName3 = "Differences"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow(winName3, cv2.CV_WINDOW_AUTOSIZE)
s = np.zeros((height,width,3), np.uint8)
t0 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
 
while True:
    
  s = cam.read()[1]
  cv2.imshow(winName,s)
  t = cv2.cvtColor(s,cv2.COLOR_RGB2GRAY)
  c = cv2.absdiff(t, t0)
  c[c < thres] = 0
  c[c >= thres] = 200
  cv2.imshow( winName3,c)
  total = np.sum(c)/200
  if total > trigger:
    print ("Movement")
  t0 = t
  key = cv2.waitKey(10)
