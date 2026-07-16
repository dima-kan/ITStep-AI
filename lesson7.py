import numpy as np
import cv2
from ultralytics import YOLO

# Завдання 1
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/crop-seg.jpg
# Покажіть усі маски рослин з підписами назви цієї
# рослини.
# Покажіть також самі рослини, для цього застосуйте
# маску, і всі зайві пікселі замініть на 255(зробити білий фон)


# image = cv2.imread('data/lesson_seg/crop3.jpg')
# model = YOLO("data/lesson_seg/crop-seg.pt")
# cv2.imshow("orig", image)
#
# results = model.predict(
#     image,
#     device="cuda"
# )
#
#
#
#
#
# result = results[0]
#
# res_img = result.plot()
# cv2.imshow("res", res_img)
# print(result)
#
#
# masks = result.masks
# print(masks)
#
# masks_data = masks.data
# masks_data = masks_data.cpu().numpy()
#
# height, width, colors = image.shape
#
#
# for i in range(len(masks_data)):
#     mask = masks_data[i]
#     mask = cv2.resize(mask, (width,height))
#     mask = mask.astype(np.bool)
#     new_image = image.copy()
#     new_image[~mask] =255
#
#     cv2.imshow(f"plant{i}", new_image)
#
#
# cv2.waitKey(0)



image = cv2.imread('data/lesson_seg/crop3.jpg')
model = YOLO("data/lesson_seg/crop-seg.pt")

results = model.predict(
    image,
    device="cuda"
)


result = results[0]

res_img = result.plot()
cv2.imshow("res", res_img)
print(result)

masks = result.masks

masks_data = masks.data
masks_data = masks_data.cpu().numpy()
mask_list = []
for mask in masks_data:
    mask_sum = mask.sum()
    mask_list.append(mask_sum)

print(mask_list)

big_mask = max(mask_list)
print(big_mask)

for i in range(len(mask_list)):
    if big_mask == mask_list[i]:
        break

print(i)

mask3 = masks_data[i]

mask_uint = mask3.astype(np.uint8)
mask_uint *=255
cv2.imshow("mask", mask_uint)

cv2.waitKey(0)