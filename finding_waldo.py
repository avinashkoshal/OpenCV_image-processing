import cv2

img = cv2.imread('images/finding_w.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
waldo = cv2.imread('images/waldo.png')
gray_waldo = cv2.cvtColor(waldo, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_img, gray_waldo, cv2.TM_CCOEFF)
x, y, w, h = cv2.minMaxLoc(result)
left = w
right = (w[0]+50, w[1]+50)
cv2.rectangle(img, left, right, (0,0,255), 3)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()   