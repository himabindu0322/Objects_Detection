# Frontend - AI Object Detection System 🎨

This is the frontend for the AI Object Detection System built using HTML, CSS, and JavaScript.

The frontend provides:
- Image upload detection
- Live webcam detection
- Real-time AI output display
- User-friendly interface

It connects with the FastAPI backend to perform AI object detection using YOLOv8.

---

# ⚙️ Technologies Used

- HTML5
- CSS3
- JavaScript
- Fetch API

---

# 📂 Frontend Structure

frontend/

│

   ├── index.html
   
   ├── style.css
   
   ├── script.js
│

---

# 🚀 Features

✅ Image Object Detection  
✅ Live Camera Detection  
✅ Real-Time AI Output  
✅ Responsive UI  
✅ Browser Webcam Support  
✅ Full Stack Integration  
✅ Real-Time Bounding Boxes

---

# 🖥️ Frontend Preview

The frontend contains:

- Image upload section
- Detect Image button
- Live webcam detection section
- Real-time detected output display

---

# ▶️ Run Frontend

Open terminal inside frontend folder:

```bash id="m4q8vk"
python -m http.server 5500

# 📄 index.html
Contains:

UI structure
Image upload section
Webcam section
AI detection output section
# 🎨 style.css
Contains:

UI styling
Layout design
Video and image styling
Button styles
Responsive alignment

# ⚡ script.js
Handles:

Image upload requests
Camera access
Live frame processing
API communication
Real-time detection updates

# 📸 Workflow

1️⃣ User uploads image or starts webcam
2️⃣ Frontend captures image/frame
3️⃣ Sends data to backend API
4️⃣ YOLOv8 detects objects
5️⃣ Detected output is displayed in browser

