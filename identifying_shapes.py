import cv2

img = cv2.imread('images/i_shapes.png', 0)
cv2.imshow('img', img)
cv2.waitKey(0)

ret, thresh = cv2.threshold(img, 127, 255, 1)
cnt, h = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for c in cnt:
	# get approximate polygons
	approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)
	if len(approx) == 3:
		shape_name = 'Triangle'
		cv2.drawContours(img, [c], 0, (0,255,0), -1)
		# Find contour center to plac text at the center
		M = cv2.moments(c)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(img, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

	elif len(approx) == 4:
		x,y,w,h = cv2.boundingRect(c)
		M = cv2.moments(c)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		# check if it is square or rectangle
		if abs(w-h) <= 3:
			shape_name = 'Square'
			cv2.drawContours(img, [c], 0, (0,125,255), -1)
			cv2.putText(img, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
		else: 
			shape_name = 'Rectangle'
			cv2.drawContours(img, [c], 0, (0,125,255), -1)
			M = cv2.moments(c)
			cx = int(M['m10'] / M['m00'])
			cy = int(M['m01'] / M['m00'])
			cv2.putText(img, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

	elif len(approx) == 10:
		shape_name = 'Star'
		cv2.drawContours(img, [c], 0, (255,255,0), -1)
		M = cv2.moments(c)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(img, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

	elif len(approx) >= 15:
		shape_name = 'circle'
		cv2.drawContours(img, [c], 0, (255,255,0), -1)
		M = cv2.moments(c)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(img, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
	cv2.imshow('identifying shapes', img)
	cv2.waitKey(0)

cv2.destroyAllWindows()