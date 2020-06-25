import cv2
import numpy as np

img = cv2.imread('images/d.png')
cv2.imshow('img', img)
''' Blurring function needs a kernel

'''
a=img.copy()
kernel = np.ones((3,3), np.float32)/9
blur = cv2.filter2D(a, -1, kernel)
cv2.imshow('blurred', blur)

gaussian = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('gaussian', gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()