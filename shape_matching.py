import cv2
import numpy as np

''' shape matching takes two images as input:
         1) Tempelate image(image to be searched)
         2) second image (in which tempelate is searched)

     cv2.matchShapes(contour tempelate, contour, method, method parameter)
     Tempelate: this is our reference contour that we are trying to find 
     Contour: the image we are checking against
     Method: type of contour matching
     Method Parameter: default as 0.0


'''
img1 = np.zeros((400, 400, 3), dtype = 'uint8')
tempelate = cv2.rectangle(img1, (20,200), (200,20), (0,255,0), -1)
cv2.imshow('tempelate', tempelate)
cv2.waitKey(0)
tempelate_gray = cv2.cvtColor(tempelate, cv2.COLOR_BGR2GRAY)

img2 = np.zeros((400, 400, 3), dtype = 'uint8')
tomatch = cv2.rectangle(img2, (15,150), (150,15), (0,255,0), -1)
tomatch = cv2.circle(tomatch, (300,200), 75, (0,255,0), -1)
cv2.imshow('tomatch', tomatch)
cv2.waitKey(0)
tomatch_gray = cv2.cvtColor(tomatch, cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(tempelate_gray, 127, 255, 0)
ret2, thresh2 = cv2.threshold(tomatch_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
contours = contours[0]
cnt, h =cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for c in cnt:
	match = cv2.matchShapes(contours, c, 1, 0.0)
	if match < 0.15:
		closest_contour = c
	else:
		closest_contour = []
cv2.drawContours(tomatch, [closest_contour], -1, (0, 0, 255), 3)
cv2.imshow('output', tomatch)
cv2.waitKey(0)

cv2.destroyAllWindows()