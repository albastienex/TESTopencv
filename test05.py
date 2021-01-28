import cv2
import numpy as np 
from matplotlib import pyplot as plt  #matplotlib初始設定
img = cv2.imread('test.jpg',1)
b = cv2.imread('test.jpg',1)
img1 =b[10:20, 10:30]
img2 =b[20:10, 60:70]
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
b[100:200,700:1000]=dst
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow( 'test', img)
cv2.imshow('b',b)
cv2.waitKey(0)
cv2.destroyWindow()