import cv2
import numpy as np 

img = cv2.imread('images/d.png', 0)
cv2.imshow('img', img)

''' Thresholding is a act of converting an image to binary form
    
    cv2.threshold(img, Threshold_Value, Max_value, Threshold_Type)
    here Threshold_value is the value above that every value becomes 255 (White) and
    everything below becomes 0 (Black)
 
'''
ret, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', threshold)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()