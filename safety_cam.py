import cv2
import math
from ultralytics import YOLO
import cvzone

# 1. LOAD THE BRAIN
# We use the "Nano" model (yolov8n.pt) because it runs fast on laptops.
# It will download automatically the first time you run this.
model = YOLO("yolov8n.pt")

# 2. OPEN THE EYE (Webcam)
# 0 is usually your default laptop camera.
cap = cv2.VideoCapture("site_safety.mp4") # For video file
cap.set(3, 1280) # Width
cap.set(4, 720)  # Height

# 3. THE LABELS (What it knows)
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    # Read one frame from the camera
    success, img = cap.read()
    
    # ASK THE AI: "What do you see?"
    results = model(img, stream=True)
    
    # DRAW THE ANSWERS
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # 1. Get the coordinates of the box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # 2. Get Confidence (How sure is the AI?)
            conf = math.ceil((box.conf[0] * 100)) / 100
            
            # 3. Get Class Name (What object is it?)
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            # 4. LOGIC: Only care about PEOPLE for safety
            if currentClass == "person" or currentClass == "backpack": 
                # Draw the box
                cvzone.cornerRect(img, (x1, y1, x2-x1, y2-y1), l=9, rt=5)
                # Put text above the box
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    # Show the video
    cv2.imshow("Antwerp Safety Eye", img)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break