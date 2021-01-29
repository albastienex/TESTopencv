import cv2
import numpy as np 
from matplotlib import pyplot as plt  

img = cv2.imread('test.jpg',1)
cv2.imshow('test',img)


face =img[10:300, 200:400]   #選取範圍
cv2.imshow('face',face)

cv2.waitKey(0)     
cv2.destroyAllWindows()   
