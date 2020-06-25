import cv2
import numpy as np 

''' we can use OpenCV functions to draw different Shaps 
    like line, rectangle, circle etc
'''
# Create an image
# here i have created an image of 400*400 and having
# 3 channels and in OpenCV datatype = uint8
img = np.zeros((400, 400, 3), dtype = 'uint8')
a = img.copy()
line = cv2.line(a, (50,50), (350,350), (0, 0, 255), 3)
line_ = cv2.line(a, (50,350), (350,50), (0, 0, 255), 3)
''' here first argument is img itself then starting x,y ending x,y
    after that color and finally thickness 
'''
cv2.imshow('line', line)
# Drawing rectangle
b = img.copy()
rectangle = cv2.rectangle(b,(50, 50), (350, 350), (0, 0, 255), 3)
cv2.imshow('rectangle', rectangle)

# Drawing cirlce
c = img.copy()
# calculating the  center of img
(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))
circle = cv2.circle(c, (x,y), (120), (0, 0, 255), 3)
cv2.imshow('circle', circle)

# a single image having line rectangle and circle
d = img.copy()
line_1 = cv2.line(d, (50,50), (350,350), (0, 0, 255), 3)
line_ = cv2.line(d, (50,350), (350,50), (0, 0, 255), 3)
rectangle_1 = cv2.rectangle(d,(50, 50), (350, 350), (0, 0, 255), 3)
circle_ = cv2.circle(d, (x,y), (60), (0, 0, 255), 3)
circle_1 = cv2.circle(d, (x,y), (120), (0, 0, 255), 3)
cv2.imshow('combined', circle_1)

cv2.waitKey(0)
cv2.destroyAllWindows()