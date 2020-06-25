import numpy as np
import cv2

image = cv2.imread('images/car.png')

# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)


## TODO: Define our color selection boundaries in RGB values
lower_green = np.array([0,210,0]) 
upper_green = np.array([250,255,250])

mask = cv2.inRange(image, lower_green, upper_green)

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]
# ### Mask and add a background image
# Load cv2.imreadund image, and convert it to RGB 
background_image = cv2.imread('images/1.jpg')

## TODO: Crop it or resize the background to be the right size (450x660)
crop_background = background_image[0:212, 0:305]
crop_background[mask == 0] = [0, 0, 0]

## TODO: Add the two images together to create a complete image!
complete_image = masked_image + crop_background
cv2.imshow('img', complete_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
