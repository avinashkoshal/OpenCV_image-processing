import cv2

img = cv2.imread('images/house.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 50, 120)
cv2.imshow('edge', edge)
cv2.waitKey(0)
''' cv2.findContours(img, retrieval_mode, approximation_mode)
    retrieval_mode : external - stores only extrnal contours
                     list     - stores all contours

    approximation method : chain approx none - stores all boundary points
                           chain approx simple - stores only start and ending points
'''
contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print('Numbers of contours are : ', len(contours))
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()