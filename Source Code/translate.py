import argparse
import imutils
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])

#shift image down
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted down image", shifted)
cv2.waitKey(0)

#shift image up
shifted = imutils.translate(image, 0, -100)
cv2.imshow("Shifted up image", shifted)
cv2.waitKey(0)

#shift image left
shifted = imutils.translate(image, -100, 0)
cv2.imshow("Shifted left image", shifted)
cv2.waitKey(0)

#shift image right
shifted = imutils.translate(image, 100, 0)
cv2.imshow("Shifted right image", shifted)
cv2.waitKey(0)

#shift image right and down
shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted right image", shifted)
cv2.waitKey(0)