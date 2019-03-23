from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])


# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)
cv2.waitKey(0)

# create the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

#plot the graph
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("No of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)