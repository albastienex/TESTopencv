import cv2
import numpy as np

img=np.zeros((512,512,3), np.uint8)     #512*512*3 

cv2.line(img,(0,0),(500,500),(255,0,0),5)    #在圖上畫線              

cv2.rectangle(img,(100,100),(300,300),(0,255,0),3) #在圖上畫矩形

cv2.circle(img,(200,200),150,(100, 100,100),2) #畫圓

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) #橢圓 


cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyWindow()