import cv2
import numpy as np

image = cv2.imread("data/lesson2/darken.png")

cv2.imshow("orig", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)


v_equalized = cv2.equalizeHist(v)

new_hsv = cv2.merge((h, s, v_equalized))

result = cv2.cvtColor(
    new_hsv,
    cv2.COLOR_HSV2BGR
)

cv2.imshow("histogram", result)


v_float = v.astype(np.float32)

v_float *= 1.3

v_float = np.clip(v_float, 0, 255)

v_float = v_float.astype(np.uint8)

new_hsv = cv2.merge((h, s, v_float))

result_bright = cv2.cvtColor(
    new_hsv,
    cv2.COLOR_HSV2BGR
)

cv2.imshow("+30%", result_bright)


cv2.waitKey(0)