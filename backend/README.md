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
└── outputs/

---

# 📦 Installation

## Create Virtual Environment

```bash
python -m venv venv

##  Run Backend Server

uvicorn main:app --reload


python -m venv venv
