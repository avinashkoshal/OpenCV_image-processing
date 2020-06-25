import cv2
import numpy as np

img = cv2.imread('images/d.png')
cv2.imshow('img', img)

''' We need an array to be added to or subtracted from Images
    this array needs to be the same size of original image
'''
m = np.ones(img.shape, dtype = 'uint8') * 75

add = cv2.add(img, m)
cv2.imshow('added', add)

sub = cv2.subtract(img, m)
cv2.imshow('sub', sub)

cv2.waitKey(0)
cv2.destroyAllWindows()