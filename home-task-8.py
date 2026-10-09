import ultralytics
import cv2

model = ultralytics.YOLO(r"data/lesson_seg/brain-tumor-seg.pt")

img = cv2.imread(r"data/lesson_seg/tumor1.jpg")

result = model.predict(img, device="cuda:0")[0]

mask = result.masks.data[0].cpu().numpy().astype("uint8") * 255
mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

pixels = cv2.countNonZero(mask)
area = pixels * 0.0025

if area < 10:
    name = "small"
elif area <= 25:
    name = "middle"
else:
    name = "large"

tumor = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow(name, tumor)
cv2.waitKey(0)