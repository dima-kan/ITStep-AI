import cv2
import numpy as np
# Завдання 1
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# розмір зображення, тип даних, максимальну та мінімальну
# інтенсивність пікселів, саме зображення з підписом.



image = cv2.imread(
    "data/lesson1/Lenna.png",
    cv2.IMREAD_GRAYSCALE,
)
#
# print(image.dtype)
# print(image.shape)
#
# print(image.max())
# print(image.min())






# Завдання 2
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# такі зображень:
#  Верхній лівий кут розміром 100х50


# segment = image[0:101,0:51]
#
#
# cv2.imshow("segment", segment)
# cv2.waitKey(0)

#  Центральний квадрат розміром 100х100

# segment2 = image[78:178,78:178]
#
#
# cv2.imshow("segment", segment2)
# print(segment2.shape)
# cv2.waitKey(0)

#  Верхню половину

# segment3 = image[:128,:256]
# cv2.imshow("segment", segment3)
# print(segment3.shape)
# cv2.imshow("segment", segment3)
# cv2.waitKey(0)
#  Нижню половину

# segment4 = image[128:257,:256]
# cv2.imshow("segment", segment4)
# print(segment4.shape)
# cv2.imshow("segment", segment4)
# cv2.waitKey(0)


#  Ліву половину

# segment5 = image[:256,0:129]
# cv2.imshow("segment", segment5)
# print(segment5.shape)
# cv2.imshow("segment", segment5)
# cv2.waitKey(0)


#  Праву половину


# segment6 = image[:256,128:257]
# cv2.imshow("segment", segment6)
# print(segment6.shape)
# cv2.imshow("segment", segment6)
# cv2.waitKey(0)

# image[:20, :] =0
# image[235:256,:]= 255
# cv2.imshow("Lenna", image)
# cv2.waitKey(0)

# image[:, 0:20] = 0
# image[:,240:257]= 0
# cv2.imshow("image", image)
# cv2.waitKey(0)


# image[:50,:] = 0
# image[220:257,:]= 0
# image[:,0:60] = 0
# image[:,200:257] = 0
# cv2.imshow("image", image)
# cv2.waitKey(0)

# вдання 4
# Відкрийте зображення data/Lenna.png. Створіть маску для
# пік селів з інтенсивністю більше 128 та виведіть її. Також
# виведіть заперечення цієї маски.
# На оригінальному зображенні, усі пікселі які не
# відповідають масці замініть на 0 та виведіть результат


# mask = image > 128
# print(mask)

# mask = mask.astype(np.uint8)
# print(mask)
#
# cv2.imshow("image", mask*255)
# cv2.waitKey(0)

# image[~mask] = 0
# cv2.imshow("image",image)
# cv2.waitKey(0)


new_image = (image/255)**2 * 255
print(new_image.dtype)
new_image = new_image.astype(np.uint8)
cv2.imshow("image", new_image)
cv2.waitKey(0)