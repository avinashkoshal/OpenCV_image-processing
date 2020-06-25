import cv2
import numpy as  np 

img = cv2.imread('images/wave.png')
cv2.imshow('img', img)
h, w = img.shape[:2]
(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))

''' just like in translation we have a matrix used in rotation called rotation matrix

           | cos0  -sin0 |
       m = | sin0   cos0 |

       0(theta) = angle of ratation
     cv2.getRotationMartrix2D((center_x, center_y), angle_of_rotation, scale)

'''
rotate = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
rotation = cv2.warpAffine(img, rotate, (w, h))
cv2.imshow('rotated', rotation)

cv2.waitKey(0)
cv2.destroyAllWindows()