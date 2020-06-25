import cv2

img = cv2.imread('images/house.png')
a = img.copy()
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
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	cv2.rectangle(a, (x,y), (x+w, y+h), (0, 0, 255), 2)
	cv2.imshow('bounding_rect', a)
cv2.waitKey(0)

for c in contours:
	accuracy = 0.03 * cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, accuracy, True)
	cv2.drawContours(img, [approx], 0, (0, 0, 255), 3)
	cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()