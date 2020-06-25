import cv2
import numpy as np 

img = cv2.imread('images/3.png')
m = np.zeros(img.shape, dtype = 'uint8')

''' There are two methods by which we can sort contours:
    1) Sort by Area - Smallest
                      Largest
    2) Sort by Spatial position - left to right

    For sorting the Contours I have used Sorted Function and 
    it take three arguments: 1) list of contours
                             2) key (on the basis of what above list is sorted) - Area
                             3) mode - ascending, descending
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 50, 120)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)
for c in sorted_contours:
	cont = cv2.drawContours(m, c, -1, (0, 255, 0), 3)
	cv2.imshow('cont', cont)
	cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()