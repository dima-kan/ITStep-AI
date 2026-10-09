import cv2

cap = cv2.VideoCapture(r"data\lesson7\meter.mp4")

fps = int(cap.get(cv2.CAP_PROP_FPS))

width = 600
height = 800

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out_writer = cv2.VideoWriter(
    "meter_result.mp4",
    fourcc,
    fps,
    (width, height),
    isColor=False,
)

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(frame, (width, height))

    gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

    bilateral = cv2.bilateralFilter(
        gray,
        9,
        75,
        75,
    )

    res = cv2.adaptiveThreshold(
        bilateral,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2,
    )

    cv2.imshow("Frame", res)

    out_writer.write(res)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
out_writer.release()
cv2.destroyAllWindows()