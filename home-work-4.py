import cv2


# img = cv2.imread("data/lesson3/sonet.png", )
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("original", gray)
#
#
# gauss = cv2.GaussianBlur(
#     gray,  # зображення з шумом
#     (3, 3),   # розмір фільтру(ядра)
#     sigmaX=1,    # наскільки важливими є далекі пікселі
# )
# cv2.imshow("gauss", gauss)
#
# result = cv2.bilateralFilter(
#     gray,          # Вхідне зображення
#     d=9,          # Діаметр околиці (9 пікселів)
#     sigmaColor=75,# Чутливість до різниці кольору
#     sigmaSpace=75 # Просторова гладкість
# )
#
#
# cv2.imshow("Bilateral Filter", result)
#
#
#
# res = cv2.adaptiveThreshold(
#     result,   # зображення з текстом(чорнобіле)
#     255,    #  білий колір
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
#     cv2.THRESH_BINARY,   # це просто треба вказати
#     21,   # розмір фільтру
#     2,          # наскільки піксель має відрізнятися від порогу
# )
#
#
#
# cv2.imshow("res", res)


image = cv2.imread("data/lesson3/sonet_noised.png")
cv2.imshow('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gauss = cv2.GaussianBlur(
    gray,  # зображення з шумом
    (1, 1),   # розмір фільтру(ядра)
    sigmaX=1,    # наскільки важливими є далекі пікселі
)
cv2.imshow("gauss", gauss)



result = cv2.bilateralFilter(
    gray,          # Вхідне зображення
    d=1,          # Діаметр околиці (9 пікселів)
    sigmaColor=75,# Чутливість до різниці кольору
    sigmaSpace=75 # Просторова гладкість
)
cv2.imshow("Bilateral Filter", result)


res = cv2.adaptiveThreshold(
    result,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    21,   # розмір фільтру
    3,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("res", res)

cv2.waitKey(0)
