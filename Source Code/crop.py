import argparse
import imutils
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# crop the image
# start y 15: end y 222 , start x 150: endx 400
cropped = image[15:222, 150:400]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
