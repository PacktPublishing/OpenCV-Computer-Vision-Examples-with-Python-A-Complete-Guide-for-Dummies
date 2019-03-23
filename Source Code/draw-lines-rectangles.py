import numpy as np
import cv2

#define a canvas of size 300x300 px, with 3 channels (R,G,B) and data type as 8 bit unsigned integer
canvas = np.zeros((300,300,3), dtype ="uint8")

#define color
#draw the line
#arguments are canvas/image, starting point, ending point, color, thickness(optional)
#display in cv2 window
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("The line 1", canvas)
cv2.waitKey(0)

# draw line with width
red = (0,0,255)
cv2.line(canvas,(0,0),(300,300),red, 3)
cv2.imshow("The line 2", canvas)
cv2.waitKey(0)

#draw rectangles
green = (0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("The rectangle 1", canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.rectangle(canvas,(10,10),(60,60),red, 3)
cv2.imshow("The rectangle 2", canvas)
cv2.waitKey(0)

blue = (255,0,0)
cv2.rectangle(canvas,(10,10),(60,60),blue, -1)
cv2.imshow("The rectangle 3", canvas)
cv2.waitKey(0)