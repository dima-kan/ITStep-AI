import math

import cv2
import ultralytics

model = ultralytics.YOLO('yolo11s-pose.pt')

cap = cv2.VideoCapture(r'data/lesson_pose/squat.mp4')

success, img = cap.read()

results = model.predict(img, device="cuda")
result = results[0]

cv2.imshow('first frame', result.plot())

xy = result.keypoints.xy
xy = xy.cpu().numpy()
xy = xy[0]
xy = xy.astype(int)

x1, y1 = xy[11]
x2, y2 = xy[13]
x3, y3 = xy[15]

print(x1, y1, x2, y2, x3, y3)

angle_down = 90
angle_up = 160

total_squats = 0
is_down = False

while True:
    success, frame = cap.read()

    if not success:
        break

    results = model.predict(frame, device="cuda")
    result = results[0]

    xy = result.keypoints.xy
    xy = xy.cpu().numpy()
    xy = xy[0]
    xy = xy.astype(int)

    x1, y1 = xy[11]
    x2, y2 = xy[13]
    x3, y3 = xy[15]

    a1 = math.atan2(y1 - y2, x1 - x2)
    a3 = math.atan2(y3 - y2, x3 - x2)
    angle = abs(math.degrees(a1 - a3))
    if angle > 180:
        angle = 360 - angle

    if angle < angle_down:
        is_down = True

    if angle > angle_up and is_down:
        total_squats = total_squats + 1
        is_down = False

    cv2.circle(frame, (x1, y1), 12, (255, 0, 0), -1)
    cv2.circle(frame, (x2, y2), 12, (0, 255, 0), -1)
    cv2.circle(frame, (x3, y3), 12, (0, 0, 255), -1)

    cv2.putText(
        frame,
        f"squats: {total_squats}, angle: {int(angle)}",
        (40, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow('img', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
