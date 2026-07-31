# 🚗 Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection System developed using **Python, OpenCV, MediaPipe Face Mesh, NumPy, and Pygame**. The system continuously monitors the driver's eyes through a webcam, calculates the **Eye Aspect Ratio (EAR)**, and triggers an alarm when prolonged eye closure is detected to help prevent accidents caused by fatigue.

---

## 📌 Features

- 👁️ Real-time face and eye tracking
- 📷 Live webcam monitoring
- 🧠 Facial landmark detection using MediaPipe Face Mesh
- 📊 Eye Aspect Ratio (EAR) calculation
- 😴 Driver drowsiness detection
- 🔔 Audio alarm for prolonged eye closure
- 💻 Live display of EAR value
- ⚡ Fast and lightweight implementation

---

## 🛠️ Technologies Used

- Python 3.12
- OpenCV
- MediaPipe Face Mesh
- NumPy
- Pygame

---

## 📂 Project Structure

```
Driver-Drowsiness-Detection/
│
├── driver_drowsiness.py
├── alarm.wav
├── requirements.txt
├── README.md
├── .gitignore
└── images/
    └── output.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/koushikmunna11-rgb/Driver-Drowsiness-Detection.git
```

Move into the project directory.

```bash
cd Driver-Drowsiness-Detection
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

Install the required libraries.

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python driver_drowsiness.py
```

Press **Q** to exit the application.

---

## 🔍 How It Works

1. The webcam captures live video frames.
2. OpenCV processes each frame.
3. MediaPipe Face Mesh detects 468 facial landmarks.
4. Eye landmarks are extracted from the detected face.
5. The Eye Aspect Ratio (EAR) is calculated.
6. If the EAR remains below a predefined threshold for several consecutive frames, the system identifies the driver as drowsy.
7. An alarm sound is played and a warning message is displayed.

---

## 📊 Eye Aspect Ratio (EAR)

The Eye Aspect Ratio is used to determine whether the driver's eyes are open or closed.

- Normal eyes → Higher EAR
- Closed eyes → Lower EAR

When the EAR remains below the threshold for a continuous period, the driver is considered drowsy.

---

## 🎯 Applications

- Smart Vehicles
- Driver Safety Systems
- Transportation Industry
- Fleet Monitoring
- Accident Prevention
- AI-based Safety Solutions

---

## 🚀 Future Improvements

- Yawning detection
- Head pose estimation
- Mobile application integration
- Email/SMS emergency alerts
- Driver identity recognition
- Night vision support
- Drowsiness event logging
- Deep Learning-based fatigue prediction

---

## 📸 Output

Add screenshots of your project inside the **images** folder.

Example:

```
images/
    output.png
```

Then display it using:

```markdown
![Output](images/output.png)
```

---

## 📦 Requirements

```
opencv-python==4.11.0.86
mediapipe==0.10.20
pygame
numpy==1.26.4
```

---

## 👨‍💻 Author

**Koushik Kattoju**

GitHub: https://github.com/koushikmunna11-rgb

**Indrani Somireddi**

GitHub: https://github.com/somireddiindrani

---

## ⭐ If you found this project useful

Please consider giving this repository a **⭐ Star** on GitHub.
