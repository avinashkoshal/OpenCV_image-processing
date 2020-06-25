import cv2
import numpy as np 

img = cv2.imread('images/wave.png')
cv2.imshow('img', img)

''' Translatios shift the image towards Right, left and diagonally
    cv2 has function wrapAffine which takes a translation matrix

           T = | 1  0  Tx |  Tx - shift along X-axis
               | 0  1  Ty |  Ty - shift along Y-axis

'''
(h, w) = img.shape[:2]
(q_h, q_w) =(int(h/4), int(w/4))
# creating translation matrix
m = np.float32([[1, 0, q_w], [0, 1, q_h]])
print(m)
translated = cv2.warpAffine(img, m, (w, h))
cv2.imshow('translated', translated)


cv2.waitKey(0)
cv2.destroyAllWindows()