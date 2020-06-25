import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('images/pizza.png')

image_copy = np.copy(image)

lower_blue = np.array([200,0,0]) 
upper_blue = np.array([255,250,250])

mask = cv2.inRange(image_copy, lower_blue, upper_blue)

# Vizualize the mask

masked_image = np.copy(image_copy)

masked_image[mask != 0] = [0, 0, 0]

background_image = cv2.imread('images/1.jpg')


# Crop it to the right size (
crop_background = background_image[0:201, 0:323]

# Mask the cropped background so that the pizza area is blocked
crop_background[mask == 0] = [0, 0, 0]

complete_image = masked_image + crop_background

cv2.imshow('img',complete_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



