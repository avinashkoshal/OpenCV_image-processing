import cv2

img = cv2.imread('images/beach.png')
cv2.imshow('original', img)
# converting images from BGR to GrayScale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

''' There is simpler method of converting BGR images to Grayscale
    at the time of reading it using imread function just provide 
    the second argument as 0 and it will conver the image into grayscale
'''
img2 = cv2.imread('images/wave.png', 0)
cv2.imshow('gray2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()