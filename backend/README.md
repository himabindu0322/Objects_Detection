# Backend - AI Object Detection System 🚀

This is the backend server for the AI Object Detection System built using FastAPI, YOLOv8, and OpenCV.

The backend handles:
- Image object detection
- Video object detection
- Live webcam frame detection
- Real-time AI inference using YOLOv8

---

# ⚙️ Technologies Used

- Python
- FastAPI
- Uvicorn
- YOLOv8
- OpenCV
- NumPy
- Ultralytics

---

# 📂 Backend Structure

backend/

│

 ├── main.py
 
 ├── detect_image.py
 
 ├── detect_video.py
 
 ├── detect_camera.py
 
 ├── requirements.txt
 
 ├── yolov8n.pt
 
│

---

# 📦 Installation

## Create Virtual Environment

```bash
python -m venv venv

##  Run Backend Server

uvicorn main:app --reload
python -m venv venv

# 🧠 YOLOv8 Model

This project uses:
yolov8n.pt
from Ultralytics for fast real-time object detection.

# 📸 API Endpoints

Home Route
GET /
Response:

{
  "message": "AI Detection API Running"
}

Image Detection
POST /detect
Upload an image and receive detected output image.

#🖥 Standalone Detection Scripts

--> Detect Objects from Image
python detect_image.py

--> Detect Objects from Video
python detect_video.py

--> Live Webcam Detection
python detect_camera.py
