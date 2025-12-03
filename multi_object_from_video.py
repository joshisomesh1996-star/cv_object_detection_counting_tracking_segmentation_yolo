import cv2
from ultralytics import YOLO

capture = cv2.VideoCapture("traffic.mp4")
model = YOLO("yolov8n.pt")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    results = model(frame, classes=[0])
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Segmentation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()