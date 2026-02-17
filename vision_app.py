import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np
from PIL import Image

st.set_page_config(page_title="HSE Safety Monitor", layout="wide")
st.title("🛡️ Port of Antwerp: Safety Vision AI")

# 1. LOAD THE BRAIN
@st.cache_resource
def load_model():
    # Make sure yolov8n.pt is in the same folder!
    return YOLO("yolov8n.pt")

model = load_model()

# 2. APP SIDEBAR
st.sidebar.header("Settings")
# Toggle between using the video file or your webcam
use_webcam = st.sidebar.toggle("Use Live Webcam", value=False)
conf_level = st.sidebar.slider("AI Confidence", 0.0, 1.0, 0.5)

# 3. VIDEO SOURCE
if use_webcam:
    cap = cv2.VideoCapture(0)
else:
    # Ensure site_safety.mp4 is in your folder
    cap = cv2.VideoCapture("site_safety.mp4")

# 4. THE LIVE FEED
st_frame = st.empty() 

# Add a 'Stop' button to end the script
if st.button("Stop Monitoring"):
    cap.release()
    st.rerun()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run Detection
    results = model.predict(frame, conf=conf_level, verbose=False)
    
    # Draw boxes on the frame
    annotated_frame = results[0].plot()

    # Convert BGR (OpenCV default) to RGB (Streamlit default)
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Display the frame in the browser
    st_frame.image(annotated_frame, channels="RGB", use_column_width=True)

cap.release()