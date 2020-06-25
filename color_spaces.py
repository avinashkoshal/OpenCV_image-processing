import cv2

img = cv2.imread('images/d.png')

''' OpenCV store images as B G R
     
         0    1     2
         B    G     R

By providing the co-ordinates i.e the x and y value we can get 
the B G R value corresponding to that pixel point

'''
print(img.shape)
# calculating the center point
(x,y) = (int(img.shape[1]/2), int(img.shape[0]/2))
# getting the B G R values of center of image
(B, G, R) = img[x, y]
print('Blue = {}, Green = {}, Red = {}'. format(B, G, R))

''' we can also get the individual Blue Green and Red 
    channels of an image using cv2.split() function and 
    then we can merge them back using cv2.merge()
 
'''
# Splitting
(B, G, R) = cv2.split(img)
cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)
# Merging
merged = cv2.merge((B, G, R))
cv2.imshow('merged', merged)

cv2.waitKey(0)
cv2.destroyAllWindows()