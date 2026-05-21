from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from ultralytics import YOLO

import shutil
import cv2
import numpy as np
import uuid
import os

app = FastAPI()

# ENABLE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LOAD YOLO MODEL
model = YOLO("yolov8n.pt")

# HOME ROUTE
@app.get("/")
def home():
    return {"message": "AI Detection API Running"}

# IMAGE DETECTION
@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    unique_id = str(uuid.uuid4())

    input_path = f"input_{unique_id}.jpg"

    output_path = f"output_{unique_id}.jpg"

    # SAVE IMAGE
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # RUN YOLO
    results = model(input_path)

    # SAVE DETECTED IMAGE
    results[0].save(filename=output_path)

    return FileResponse(
        output_path,
        media_type="image/jpeg"
    )

# LIVE CAMERA DETECTION
@app.post("/detect-frame")
async def detect_frame(file: UploadFile = File(...)):

    contents = await file.read()

    np_array = np.frombuffer(contents, np.uint8)

    frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # RUN YOLO
    results = model(frame)

    # DRAW BOXES
    annotated_frame = results[0].plot()

    output_path = "live_output.jpg"

    cv2.imwrite(output_path, annotated_frame)

    return FileResponse(
        output_path,
        media_type="image/jpeg"
    )
