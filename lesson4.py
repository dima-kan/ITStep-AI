# import cv2
#
# image = cv2.imread("data/lesson3/notes.png")
#
# image = cv2.resize(image, (600, 600))
#
# # cv2.imshow("orig", image)
#
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("gray", gray)
#
# # threshold = 45
# # mask = gray < threshold
# # gray[mask] = 0
# # gray[~mask] = 255
#
#
# cv2.imshow("binar", gray)
#
# # gauss = cv2.GaussianBlur(
# #     gray,  # зображення з шумом
# #     (3, 3),   # розмір фільтру(ядра)
# #     sigmaX=3,    # наскільки важливими є далекі пікселі
# # )
# # cv2.imshow("gauss", gauss)
#
# bilat = cv2.bilateralFilter(
#     gray,  # зображення з шумом
#     d=4,    # розмір фільтру
#     sigmaColor=75,   # наскільки важливі пікселі іншого кольору
#     sigmaSpace=50,   # наскільки важливими є далекі пікселі
# )
#
# cv2.imshow("bilat", bilat)
#
#
#
#
# res = cv2.adaptiveThreshold(
#     bilat,   # зображення з текстом(чорнобіле)
#     255,    #  білий колір
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
#     cv2.THRESH_BINARY,   # це просто треба вказати
#     11,   # розмір фільтру
#     2,          # наскільки піксель має відрізнятися від порогу
# )
#
# cv2.imshow("adaptive", res)
#
# cv2.waitKey(0)
import cv2

# Завдання 2
# Відкрийте зображення data/lesson3/sudoku.jpg. Проведіть
# для нього бінарізацію, а саме
#  CLAHE
#  гаусове розмиття
#  адаптивна бінарізація
#  NLMean
# Самостійно підберіть параметри, збережіть результат.
# Порівняйте результати для гаусової та середньої адаптивної
# бінарізації




image =cv2.imread('data/lesson3/sudoku.jpg')
cv2.imshow('image',image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

result = clahe.apply(gray)

cv2.imshow("CLAHE Result", result)
cv2.waitKey(0)


cv2.imshow("CLAHE Result", result)

gauss = cv2.GaussianBlur(gray,(3,3),1.5)
cv2.imshow("Gauss", gauss)

res = cv2.adaptiveThreshold(
    result,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)
cv2.imshow("Adaptive Threshold", res)

res = cv2.adaptiveThreshold(
    gauss,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+gauss", res)


result_gray = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

cv2.imshow("fastNlMeansDenoising", result_gray)

res2 = cv2.adaptiveThreshold(
    result_gray,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)
cv2.imshow("adapt threshold", res2)


cv2.waitKey(0)
