import cv2
from ultralytics import YOLO
import numpy as np
from collections import defaultdict, deque

model = YOLO("yolov8n.pt")
capture = cv2.VideoCapture("walking.mp4")

id_mapping = {}
nex_id = 1

trail = defaultdict(lambda: deque(maxlen=30))
appear = defaultdict(int)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    res = model.track(frame, classes=[0], persist=True, verbose=False)
    annotated_frame = frame.copy()

    if res[0].boxes.id is not None:
        boxes = res[0].boxes.xyxy.cpu().numpy()
        ids = res[0].boxes.id.cpu().numpy()

        for box, tid in zip(boxes, ids):
            x1, y1, x2, y2 = map(int, box)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            appear[tid] += 1

            if appear[tid] >= 5 and tid not in id_mapping:
                id_mapping[tid] = nex_id
                nex_id += 1

            if tid in id_mapping:
                sid = id_mapping[tid]

                trail[tid].append((cx, cy))

                trail_points = list(trail[tid])
                for i in range(1, len(trail_points)):
                    cv2.line(annotated_frame,
                             trail_points[i-1],
                             trail_points[i],
                             (0, 255, 255), 2)   
                

                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f"ID: {sid}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                cv2.circle(annotated_frame, (cx, cy), 5, (255, 0, 0), -1)

    cv2.imshow("Annotated Frame", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
