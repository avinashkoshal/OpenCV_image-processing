import cv2
import matplotlib.pyplot as plt
import numpy as np

filter  = cv2.imread('images/i_f.png')
print(filter.shape)

filter = cv2.resize(filter, (300,300))

# It converts the BGR color space of image to HSV color space 
hsv = cv2.cvtColor(filter, cv2.COLOR_BGR2HSV) 
    
# Threshold of blue in HSV space 
lower = np.array([0, 150, 150])         
upper = np.array([15, 255, 255])    
 # preparing the mask to overlay 
mask = cv2.inRange(hsv, lower, upper) 
 
# The black region in the mask has the value of 0, 
# so when multiplied with original image removes all non-blue regions 
result = cv2.bitwise_and(filter, filter, mask = mask) 

cv2.imshow('original', filter)
cv2.waitKey(0)

cv2.imshow('mask', mask)
cv2.waitKey(0)

cv2.imshow('result', result)
cv2.waitKey(0)

cv2.destroyAllWindows()


