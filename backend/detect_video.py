import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Input video
video_path = "video.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

# Check video
if not cap.isOpened():
    print("Error opening video")
    exit()

# Video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Save output video
out = cv2.VideoWriter(
    "output_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO detection
    results = model(frame)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Save frame
    out.write(annotated_frame)

    # Show frame
    cv2.imshow("Video Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing completed")
