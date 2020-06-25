import cv2

img = cv2.imread('images/d.png')
cv2.imshow('original', img)

''' Pyramiding images refers to either upscaling(enlarging) or downscaling(shrinking images)
    It allows us to scale images easily and quickly
    cv2.pyrUp - enlarge the image
    cv2.pyrDown - shrinks tha image

'''

small = cv2.pyrDown(img)
cv2.imshow('small', small)

smaller = cv2.pyrDown(small)
cv2.imshow('smaller', smaller)

more_smaller = cv2.pyrDown(smaller)
cv2.imshow('more_smaller', more_smaller)

up = cv2.pyrUp(more_smaller)
up_up = cv2.pyrUp(up)
up_ = cv2.pyrUp(up_up)
cv2.imshow('up', up_)

cv2.waitKey(0)
cv2.destroyAllWindows()