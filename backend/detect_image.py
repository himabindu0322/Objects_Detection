from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Image path
image_path = "test.jpg"

# Run detection
results = model(image_path)

# Show results
results[0].show()

# Save output
results[0].save(filename="output.jpg")

print("Detection completed")
