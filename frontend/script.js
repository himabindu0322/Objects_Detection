let stream;
let interval;

// IMAGE DETECTION
async function detectObjects() {

    const fileInput = document.getElementById("imageInput");

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select image");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/detect",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Detection failed");
        }

        const blob = await response.blob();

        const imageURL = URL.createObjectURL(blob);

        document.getElementById("outputImage").src = imageURL;

    } catch (error) {

        console.error(error);

        alert("Image detection failed");

    }
}

// START CAMERA
async function startCamera() {

    const video = document.getElementById("video");

    try {

        stream = await navigator.mediaDevices.getUserMedia({
            video: true
        });

        video.srcObject = stream;

        await video.play();

        setTimeout(() => {
            processFrames();
        }, 1000);

    } catch (error) {

        console.error(error);

        alert("Camera access failed");

    }
}

// PROCESS LIVE FRAMES
function processFrames() {

    const video = document.getElementById("video");

    const canvas = document.getElementById("canvas");

    const ctx = canvas.getContext("2d");

    const liveOutput = document.getElementById("liveOutput");

    if (interval) {
        clearInterval(interval);
    }

    interval = setInterval(async () => {

        try {

            if (video.videoWidth === 0) return;

            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            ctx.drawImage(video, 0, 0);

            const blob = await new Promise(resolve =>
                canvas.toBlob(resolve, "image/jpeg")
            );

            const formData = new FormData();

            formData.append("file", blob, "frame.jpg");

            const response = await fetch(
                "http://127.0.0.1:8000/detect-frame",
                {
                    method: "POST",
                    body: formData
                }
            );

            if (!response.ok) {
                throw new Error("Frame detection failed");
            }

            const imageBlob = await response.blob();

            const imageURL = URL.createObjectURL(imageBlob);

            // FORCE UPDATE IMAGE
            liveOutput.src = "";

            setTimeout(() => {
                liveOutput.src = imageURL;
            }, 10);

        } catch (error) {

            console.error(error);

        }

    }, 700);
}
