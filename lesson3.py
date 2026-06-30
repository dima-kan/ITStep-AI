# import numpy as np
# import cv2
# # Завдання 1
# # Відкрийте зображення data/lesson2/marbles.png.
# # Використайте кольорову сегментацію для отримання масок до
# # кульок:
# #  синього кольору
# #  зеленого і червоного
# #  чорного
# #  білого
# #  усіх кульо
#
#
# image = cv2.imread('data/lesson2/marbles.png')
#
# cv2.imshow('image', image)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# # lower = (0, 0, 0)
# # upper = (100, 100, 50)
# # mask = cv2.inRange(hsv, lower, upper)
# # cv2.imshow('mask', mask)
# # cv2.waitKey(0)
#
# lower = (0, 0, 200)
# upper = (150, 30, 255)
# mask = cv2.inRange(hsv, lower, upper)
# cv2.imshow('mask', mask)
# cv2.waitKey(0)
#
#
#
#
# #
# # lower = (0,100,150)
# # upper = (7,255,255) # червоний
# # mask_red = cv2.inRange(hsv, lower, upper)
# #
# # lower = (35,90,80)
# # upper = (90,255,255)
# #
# # mask_green = cv2.inRange(hsv, lower, upper)
# # cv2.imshow('mask_green', mask_green)
# #
# # cv2.imshow('mask_red', mask_red)
# #
# # mask_red_green = cv2.bitwise_or(mask_red, mask_green)
# # cv2.imshow('mask_red_green', mask_red_green)
# # cv2.waitKey(0)
#
# # lower = (100, 120, 110)
# # upper = (130, 255, 255)
# #
# #
# #
# # mask = cv2.inRange(hsv, lower, upper)
# #
# # cv2.imshow('mask', mask)
# #
# # cv2.waitKey(0)
