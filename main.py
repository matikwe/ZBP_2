import cv2
import numpy as np

file_name = "face.png"
path = "D:\\Users\\Mateusz\\detectedImage.png"
minRange = np.array([0, 133, 77], np.uint8)
maxRange = np.array([235, 173, 127], np.uint8)
image = cv2.imread(file_name)

YCRimage = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
skinArea = cv2.inRange(YCRimage, minRange, maxRange)
detectedSkin = cv2.bitwise_and(image, image, mask=skinArea)

cv2.imwrite(path, np.hstack([detectedSkin]))
image = np.hstack([detectedSkin])
print("Matrix:")
print(image)
