'''
Author spomega
12/08/2018
'''

import cv2
import numpy as np

image = cv2.imread("images/resized.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

#image 3/4 of original size
'''
image_scaled = cv2.resize(image, None, fx=0.2, fy=0.2)
cv2.imwrite("resized.jpg", image_scaled)
cv2.imwrite("resized.png", image_scaled)
cv2.imshow('Scaling- Linear Interpolation', image_scaled)
'''
cv2.imshow("Unripe cocoa", image)

#convert bgr to hsv
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#cv2.imshow("hsv", image_hsv)

lower_range = np.array([45, 50, 50])
upper_range = np.array([72, 200, 200])

mask = cv2.inRange(image_hsv,lower_range,upper_range)
#cv2.imshow("mask", mask)

res = cv2.bitwise_and(image,image,mask = mask)
cv2.imshow("result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
