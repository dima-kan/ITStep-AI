# import ultralytics
# import cv2
#
# # Завдання 1
# # Отримайте перший кадр з файлу data\lesson8\animals.mp4
# # та виведіть його на екран.
# # Проведіть детекцію об’єктів зо допомогою YOLO та
# # виведіть результати.
# # Змініть параметри моделі conf та iou і подивіться як це
# # впливає на результат.
# # Отримайте рамки для кожного об’єкта, виріжіть їх та
# # виведіть як окремі зображення
#
#
#
# model = ultralytics.YOLO("yolo11s.pt")
#
# cap = cv2.VideoCapture(r"data\lesson8\animals.mp4")
#
# success, img = cap.read()
#
# # cv2.imshow("original", img)
#
# results = model.predict(
#     img,
#     device = "cuda:0",
#     conf = 0.5,
#     iou = 0.7
# )
#
# result = results[0]
#
# res = result.plot()
#
# print(result)
#
# cv2.imshow("result", res)
#
# boxes = result.boxes
# box1 = boxes[0]
# print(box1)
#
# cls = box1.cls
# print(cls)
#
# conf = box1.conf
# print(conf)
#
# xyxy = box1.xyxy
# print(xyxy)
#
#
#
# cls = cls.cpu().numpy()
# conf = conf.cpu().numpy()
# xyxy = xyxy.cpu().numpy().astype(int)
#
#
#
# x1, y1, x2, y2 = xyxy[0]
#
#
# box1_img = img[y1:y2, x1:x2]
#
#
# 
# names = result.names
# name = names[cls[0]]
#
# print(conf[0])
# print(name)
#
# cv2.imshow(f"{name},{conf[0]*100:.2f}", box1_img)
# cv2.waitKey(0)
#
# # for box in boxes:
# #
# #     cls = box.cls
# #
# #     conf = box.conf
# #
# #     xyxy = box.xyxy
# #
# #     cls = cls.cpu().numpy()
# #     conf = conf.cpu().numpy()
# #     xyxy = xyxy.cpu().numpy().astype(int)
# #
# #     x1, y1, x2, y2 = xyxy[0]
# #
# #     box1_img = img[y1:y2, x1:x2]
# #
# #     names = result.names
# #     name = names[cls[0]]
# #
# #     print(conf[0])
# #     print(name)
# #
# #     cv2.imshow(f"{name},{conf[0] * 100:.2f}", box1_img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# #
# # while True:
# #     success, frame = cap.read()
# #
# #     if not success:
# #         break
# #
# #     results = model.predict(
# #         frame,
# #         device="cuda:0",
# #         conf=0.5,
# #         iou=0.7
# #     )
# #
# #     result = results[0]
# #
# #     boxes = result.boxes
# #
# #     for i in range(len(boxes)):
# #
# #         box = boxes[i]
# #
# #         cls = box.cls
# #
# #         conf = box.conf
# #
# #         xyxy = box.xyxy
# #
# #         cls = cls.cpu().numpy()
# #         conf = conf.cpu().numpy()
# #         xyxy = xyxy.cpu().numpy().astype(int)
# #
# #         x1, y1, x2, y2 = xyxy[0]
# #
# #         box1_img = frame[y1:y2, x1:x2]
# #
# #         names = result.names
# #         name = names[cls[0]]
# #
# #         print(conf[0])
# #         print(name)
# #
# #         cv2.imshow(f"{name}_{i}", box1_img)
# #
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# #
# # cv2.destroyAllWindows()