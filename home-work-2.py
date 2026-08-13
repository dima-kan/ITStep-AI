import cv2
import numpy as np

image1  = cv2.imread("./data/lesson1/mask1.png")
image2 = cv2.imread("./data/lesson1/mask2.png")

mask = cv2.bitwise_or(image1, image2)


mask  = cv2.resize(mask,(1024,1024))
# segment = mask[,]


cv2.imshow("mask", mask)

print(mask.dtype)
print(mask.shape)








cv2.waitKey(0)