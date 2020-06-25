import cv2
# Reading image
img = cv2.imread('images/d.png')
# Display image
cv2.imshow('img', img)
# Write Image
cv2.imwrite('new-m.jpg', img)
# Getting Width of image
Width = img.shape[1]
# Getting Height of image
Height = img.shape[0]
# Getting Channles of image
Channles = img.shape[2]
print('The Width, Height and Channles of the Image are : {}, {}, {}'.format(Width, Height, Channles))

cv2.waitKey(0)
cv2.destroyAllWindows()