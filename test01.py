import cv2
import numpy as np 
from matplotlib import pyplot as plt  #matplotlib初始設定
img = cv2.imread('test.jpg',1)

img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #顏色轉換

# test.jpg後面直接輸入0會顯示黑白1會顯示彩色



print(img)    #從灰階叫出img可以知道圖片的大小
              #從彩色叫出img可以知道RGB組成   
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
# cv2.namedWindow('test',cv2.WINDOW_NORMAL)  #顯示的圖檔初始設定為無法更改大小，可用此語法更改

# cv2.imshow('test', img) #顯示圖檔

# cv2.imwrite('test1.jpg', img)  #跑出圖檔後以test1的檔名存取

cv2.waitKey(0)     
#這裡 cv2.waitKey 函數是用來等待與讀取使用者按下的按鍵
# ，而其參數是等待時間（單位為毫秒），若設定為 0 就表示
# 持續等待至使用者按下按鍵為止，這樣當我們按下任意按鍵之後
# ，就會呼叫 cv2.destroyAllWindows 關閉所有 OpenCV 的視窗。

cv2.destroyAllWindows()   # 關閉 'My Image' 視窗



