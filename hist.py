import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/wave.png')
cv2.imshow('img', img)

''' Cv2 has function to calculate the histogram
    cv2.calcHist([img], [channels], [mask], [size], [range])
    channels - corrrespods to B G R we can calculate for individual
    channles or all three at once by using loop

'''
# Calculating Histogram for Single channel
col0 = 'b'
col1 = 'g'
col2 = 'r'
hist = cv2.calcHist([img], [2], None, [256], [0,256])
plt.plot(hist, color = col2)
plt.show()

# Calculating Histogram for All three channels
color = ('b', 'g', 'r')
for i, col in enumerate(color):
	hist1 = cv2.calcHist([img], [i], None, [128], [0,256] )
	plt.plot(hist1, color = col)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()