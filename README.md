# 🤖 Pose Detection Web App

Welcome to the **Pose Detection Web App** — a smart, real-time system that uses your webcam to track and analyze body movements using AI! Built with a mix of Python, Flask, MediaPipe, and OpenCV, this project forms the backend brain of an interactive pose estimation platform.

---

## 🚀 What It Does

Using your webcam, this app detects human body poses in real-time — identifying keypoints like elbows, knees, shoulders, and more.

Imagine a digital skeleton following your moves — that's what this system does behind the scenes!

---

## 🛠️ Tech Stack

| Tool          | Purpose                                   |
|---------------|-------------------------------------------|
| **MediaPipe** | Real-time pose estimation                 |
| **OpenCV**    | Webcam video capture and display          |
| **Flask**     | Web API backend (coming soon for frontend)|
| **PyCharm**   | Development IDE                           |

 | File/Folder              | Description                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------- |
| **`app.py`**             | Starts the Flask web server. It has a test route (`/`) returning a simple JSON message. |
| **`pose_detector.py`**   | Contains the actual logic for detecting body pose via webcam. Uses MediaPipe + OpenCV.  |
| **`run_pose.py`**        | A quick script that imports and runs `detect_pose()` independently of Flask.            |
| **`firebase_config.py`** | (Optional) Used to connect to Firebase if you need real-time database, login, etc.      |
| **`templates/`**         | Flask uses this to load HTML files if you add a frontend (e.g., index.html).            |
| **`static/`**            | Store static assets like webcam snapshots, styles, or JS files if needed later.         |
| **`requirements.txt`**   | Keeps a list of Python packages needed so others can install them easily.               |
| **`README.md`**          | Friendly documentation that explains what the project does and how to run it.           |


You run run_pose.py to test and use pose detection separately


---

## 📦 Installation

First, make sure you have Python installed.

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
