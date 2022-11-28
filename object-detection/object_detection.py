import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
plt.ion()
img = cv2.imread('lucas.png')




# convert to hsv colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower bound and upper bound for Green color
lower_bound = np.array([22,138.72,204])   
upper_bound = np.array([90,223.63,252])
# find the colors within the boundaries
mask = cv2.inRange(hsv, lower_bound, upper_bound)

#define kernel size  
kernel = np.ones((80,80),np.uint8)
# Remove unnecessary noise from mask
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
segmented_img = cv2.bitwise_and(img, img, mask=mask)
# Find contours from the mask
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
print("read")
print(str(len(contours)))
cv2.imwrite('test.png', output)
print("done")