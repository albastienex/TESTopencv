import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('test.jpg',1)

print(img.shape)
img1=cv2.imread('test.jpg')
roi=img1[200:400,200:400]

# img[149:194,460:608]=roi
# roi=img[200:400, 200:400]
# img[100:300,100:300]=roi

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img, roi) 
plt.xticks([]), plt.yticks([]) 
plt.show()