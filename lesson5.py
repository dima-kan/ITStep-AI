import cv2
import numpy as np
# cap = cv2.VideoCapture(r"data\lesson7\text.mp4")
#
# fps = int(cap.get(cv2.CAP_PROP_FPS))
#
# width = 600
# height = 800
#
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#
# out_writer = cv2.VideoWriter(
#     "result.mp4",
#     fourcc,
#     fps,
#     (width, height),
#     isColor=True,
# )
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         break
#
#     new_frame = cv2.resize(frame, (width, height))
#
#     cv2.imshow("Frame", new_frame)
#
#     out_writer.write(new_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# cap.release()
# out_writer.release()
#



# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.

# width = 1000
# height = 1000
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         break
#
#     new_frame = cv2.resize(frame, (width, height))
#
#     gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
#
#
#
#
#
#     gauss = cv2.GaussianBlur(
#         gray,  # зображення з шумом
#         (5, 5),   # розмір фільтру(ядра)
#         sigmaX=2,    # наскільки важливими є далекі пікселі
#     )
#     cv2.imshow("gauss", gauss)
#
#     res = cv2.adaptiveThreshold(
#         gauss,  # зображення з текстом(чорнобіле)
#         255,  # білий колір
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # фільтр для обрахунку порогу(гаус)
#         cv2.THRESH_BINARY,  # це просто треба вказати
#         11,  # розмір фільтру
#         2,  # наскільки піксель має відрізнятися від порогу
#     )
#
#     cv2.imshow("Frame", res)
#
#     if cv2.waitKey(50) & 0xFF == ord("q"):
#         break


# Відкрийте відео з файлу data\lesson7shapes.mp4.
# Проведіть виділення країв на кадрах та збережіть в новий
# файл.


cap = cv2.VideoCapture(r"data\lesson7\shapes.mp4")

width = 600
height = 800


while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(frame, (width, height))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = (40,60,20)
    upper = (65,255,255)

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("green", mask)

    cv2.imshow("Frame", new_frame)




    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

