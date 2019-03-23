import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

#average blurring
blurred = np.hstack([
	cv2.blur(image, (3,3)),
	cv2.blur(image, (5,5)),
	cv2.blur(image, (7,7))])

cv2.imshow("averaged blurr", blurred)
cv2.waitKey(0)

#gaussian blurring
blurred = np.hstack([
	cv2.GaussianBlur(image, (3,3), 0),
	cv2.GaussianBlur(image, (5,5), 0),
	cv2.GaussianBlur(image, (7,7), 0)])

cv2.imshow("Gaussian blurr", blurred)
cv2.waitKey(0)

#median blurring
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])

cv2.imshow("Median blurr", blurred)
cv2.waitKey(0)

#bilateral blurring
blurred = np.hstack([
	cv2.bilateralFilter(image, 3, 21, 21),
	cv2.bilateralFilter(image, 5, 31, 31),
	cv2.bilateralFilter(image, 7, 41, 41)])

cv2.imshow("bilateral blurr", blurred)
cv2.waitKey(0)
