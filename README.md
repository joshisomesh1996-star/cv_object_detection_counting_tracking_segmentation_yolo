# 🧠 YOLOv8 Computer Vision Projects
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF4A3D?logo=yolo) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
A collection of computer vision projects built using **YOLOv8**, **OpenCV**, and **Python**, demonstrating object detection, tracking, segmentation, motion trails, and object counting.
## 🚀 Features
- Real-time object detection  
- Multi-object tracking with persistent IDs  
- Motion trails behind tracked persons  
- Instance segmentation with contour outlines  
- Unique object counting using YOLO tracker IDs  
- Clean and modular Python scripts  
## 📁 Included Scripts
| Script | Description |
|--------|-------------|
| **live_camera_feed.py** | YOLOv8 real-time detection from webcam feed. |
| **multi_object_from_video.py** | Person detection in a video file. |
| **object_counting.py** | Unique object counting using tracker IDs. |
| **people_with_trail.py** | Person tracking with motion trails. |
| **segmentation.py** | YOLOv8 segmentation + contour tracking (no bounding boxes). |
| **simple_object_detection.py** | Single-image detection example. |
## 🔧 Installation
Install dependencies: `pip install ultralytics opencv-python numpy`
## ▶️ How to Run
**Webcam Detection:** `python live_camera_feed.py`  
**Video Detection:** `python multi_object_from_video.py`  
**Object Counting:** `python object_counting.py`  
**People Tracking with Motion Trails:** `python people_with_trail.py`  
**Segmentation Tracking:** `python segmentation.py`  
**Single Image Detection:** `python simple_object_detection.py`  
Press **Q** to exit any script.
## 📦 Folder Structure
📂 your-repo  
 ├── live_camera_feed.py  
 ├── multi_object_from_video.py  
 ├── object_counting.py  
 ├── people_with_trail.py  
 ├── segmentation.py  
 ├── simple_object_detection.py  
 └── README.md  
## 💡 Enhancements
- Unique trail colors per ID  
- Transparent segmentation overlays  
- Save processed video  
- Upgrade to YOLOv8s/m for higher accuracy  
## 📜 License
Licensed under the **MIT License**.
