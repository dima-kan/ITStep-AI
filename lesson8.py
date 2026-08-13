import cv2
import ultralytics
from torch.xpu import device

# model = ultralytics.YOLO('yolo11s-pose.pt')
#
# img = cv2.imread('data/lesson_pose/human.jpg')
#
# results = model.predict(img)
# result = results[0]
#
# res_img = result.plot()
#
# # ключові точки
# keypoints = result.keypoints
#
# # ймовірності для кожної точки
# conf = keypoints.conf
#
# # print(conf)
# # print(conf.shape)  # (кількість людей, кількість точок(17))
#
# # координати xy
# xy = keypoints.xy
#
# # print(xy)
# # print(xy.shape) # (кількість людей, кількість точок(17), координати)
#
# # координати правої долоні
# xy_right_hand = xy[0, 10]  # людина 0, точка 10
# xy_right_hand = xy_right_hand.cpu()  # відключити від графічного процесора
# xy_right_hand = xy_right_hand.numpy()  # перевести у звичайний масив
#
# x, y = xy_right_hand
#
# # треба перевести в int
# x = int(x)
# y = int(y)
#
# # print(x)
# # print(y)
#
# # намалювати коло на зображення
# cv2.circle(
#     img,   # зображення де малювати коло
#     (x, y),     # координати центру
#     20,         # радіус кола
#     (255, 0, 0),  # колір у bgr(тут синій)
#     -1                 # товщина лінії(-1 означає повністю заповнене коло)
# )
#
# # накласти текст на зображення
# cv2.putText(
#     img,                  # зображення
#     'Right hand',    # текст
#     (x+30, y-30),     # нижня ліва точка початку тексту
#     cv2.FONT_HERSHEY_SIMPLEX,    # шрифт
#     0.8,          # розмір шрифту(відсоток до стандарту)
#     (0, 0, 0),      # колір у bgr(тут чорний)
#     2           # товщина ліній
#
# )
#
# xy = xy.cpu().numpy()
# # ліва стопа
# x_left_foot, y_left_foot = xy[0, 15]
#
# # праве плече
# x_right_shoulder, y_right_shoulder = xy[0, 6]
#
# # чи справді праве плече знаходиться правіше за ліву стопу
# if x_right_shoulder > x_left_foot:
#     print("праве плече знаходиться правіше за ліву стопу")
# else:
#     print("праве плече знаходиться лівіше за ліву стопу")
#
# # чи справді праве плече знаходиться вище за ліву стопу
# if y_right_shoulder < y_left_foot:
#     print("праве плече знаходиться вище за ліву стопу")
# else:
#     print("праве плече знаходиться нижче за ліву стопу")
#
# cv2.imshow('original', img)
# cv2.imshow('result', res_img)
# cv2.waitKey(0)



# Завдання 1
# Відкрийте відео data/lesson_pose/sitting.mp4
# Отримайте перший кадр
# Покажіть його, за потреби змініть розмір


model = ultralytics.YOLO('yolo11s-pose.pt')

cap = cv2.VideoCapture(r'data/lesson_pose/sitting.mp4')
success, img = cap.read()

cv2.imshow('img', img)

# Завдання 2
# Застосуйте модель YOLO Pose
# Отримайте результати (result) та виведіть їх на екран
# Використайте параметри device


results = model.predict(img)

results = model.predict(
    img,
    device = "cuda"
)

result = results[0]
# print(result)


# Завдання 3
# Користуючись методом plot() отримайте зображення з
# рамками та підписами і покажіть його.


result_img = result.plot()
#
# cv2.imshow('result_img', result_img)


# Завдання 4
# ● Отримайте інформацію про ключові точки(keypoints)
# ● Виведіть її на екран
# ● Отримайте координати точок(xy)
# ● Виведіть координати на екран разом з типом даних та
# розміром(позбудьтесь тензорів за допомогою cpu() та
# numpy())

keypoints = result.keypoints
# print(keypoints)


xy = keypoints.xy

xy = xy.cpu().numpy()

# print(xy)


# Завдання 5
# ● Отримайте координати для лівого коліна, лівої руки,
# правої руки для першого об’єкта
# ● Намалюйте ці точки на зображенні:
# ○ ліве коліно – зелений
# ○ ліва рука – червоний
# ○ права рука – білий

xy = xy[0]

xy = xy.astype(int)

x_left_knee, y_left_knee = xy[14]
x_left_hand, y_left_hand = xy[10]
x_right_hand, y_right_hand = xy[9]



cv2.circle(
    img,   # зображення де малювати коло
    center=(x_right_hand, y_right_hand),   # координати центру
    radius=15,   # радіус в пікселях
    color=(255, 255, 255),  # колір в BGR(синій)
    thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
)

cv2.circle(
    img,   # зображення де малювати коло
    center=(x_left_hand, y_left_hand),   # координати центру
    radius=15,   # радіус в пікселях
    color=(0, 0, 255),  # колір в BGR(синій)
    thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
)

cv2.circle(
    img,   # зображення де малювати коло
    center=(x_left_knee, y_left_knee),   # координати центру
    radius=15,   # радіус в пікселях
    color=(0, 255, 0),  # колір в BGR(синій)
    thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
)


cv2.imshow('img', img)

# Завдання 6
# Для кожного кадру на відео намалюйте координати для
# лівого коліна, лівої руки, правої руки
# Беріть координати для першого об’єкта
total_sitting = 0
is_sitting = True
while True:
    success,frame = cap.read()

    if not success:
        break

    results = model.predict(
        frame,
        device="cuda"
    )

    result = results[0]
    keypoints = result.keypoints

    xy = keypoints.xy
    xy = xy.cpu().numpy()

    xy = xy[0]

    xy = xy.astype(int)

    x_left_knee, y_left_knee = xy[14]
    x_left_hand, y_left_hand = xy[10]
    x_right_hand, y_right_hand = xy[9]
    x_right_knee, y_right_knee = xy[13]

    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_right_hand, y_right_hand),  # координати центру
        radius=15,  # радіус в пікселях
        color=(255, 255, 255),  # колір в BGR(синій)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_left_hand, y_left_hand),  # координати центру
        radius=15,  # радіус в пікселях
        color=(0, 0, 255),  # колір в BGR(синій)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_left_knee, y_left_knee),  # координати центру
        radius=15,  # радіус в пікселях
        color=(0, 255, 0),  # колір в BGR(синій)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_right_knee, y_right_knee),  # координати центру
        radius=15,  # радіус в пікселях
        color=(255, 0, 0),  # колір в BGR(синій)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    if y_right_knee < y_right_hand and is_sitting:
        total_sitting = total_sitting + 1

    if y_right_knee < y_right_hand:
        is_sitting = False
    else:
        is_sitting = True





    cv2.putText(
        frame,  # зображення де пишемо текст
        f"sitting:{total_sitting},sitting:{is_sitting}",  # текст
        (40,40),  # позиція, лівий нижній кут
        cv2.FONT_HERSHEY_SIMPLEX,  # шрифт
        1,  # розмір шрифту
        (255, 255, 255),  # колір в BGR
        2  # товщина ліній
    )

    cv2.imshow('img', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Завдання 7
# Під час відео обраховуйте кількість присідань.
# Вважайте що людина присіла якщо рука опустилась
# нижче коліна.
# Кількість присідань відображайте на кадрі(cv2.putText)

# Модифікуйте код щоб кількість присідань виводилась
# правильно. Для цього вам потрібно визначати чи людина
# зараз присідає чи піднімається за правилом:
# ● якщо рука нижче коліна то людина встає
# ● якщо рука вище коліна – присідає



