import cv2

img = cv2.imread('images/d.png', 0)
cv2.imshow('img', img)

edge = cv2.Canny(img, 70, 120)
cv2.imshow('edge', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()