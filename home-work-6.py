import ultralytics
import cv2

model = ultralytics.YOLO("yolo11s.pt")

width = 1000
height = 600


# Завдання 1


cap = cv2.VideoCapture(r"data\lesson8\meetings.mp4")

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(frame, (width, height))

    results = model.predict(
        new_frame,
        device="cuda:0",
        conf=0.5,
        iou=0.7,
        classes=[0],  #
    )

    result = results[0]

    res = result.plot()

    cv2.imshow("result", res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()





started = False

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(frame, (width, height))

    results = model.predict(
        new_frame,
        device="cuda:0",
        conf=0.5,
        iou=0.7,
        classes=[0],
    )

    result = results[0]

    count = len(result.boxes)

    if count == 5:
        started = True

    if started:
        res = result.plot()
        cv2.imshow("result", res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()