import cv2
import numpy as np 

img= cv2.imread('images/d.png')
cv2.imshow('original ',img)
cropped = img[20:130, 230:340]
cv2.imshow('crop', cropped)

print('shape of the image is : ',img.shape)
# Array Slicing -- slicing a particular area of an image
corner = img[0:322, 0:600]
img[0:322, 0:600] = (255, 0 ,0) # setting B = 255, G = 0, R = 0 .i.e setting and getting only blue values 
 # start Y : end Y, start X, end X

cv2.imshow(' ',corner)

cv2.waitKey(0)
cv2.destroyAllWindows()

''' Here img takes four argument 
      Y1  -- Up  
      Y2  -- Down
      X1  -- Left
      X2  -- Right

'''