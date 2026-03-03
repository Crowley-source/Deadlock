# 🔥 Deadlock — Autonomous Fire & Smoke Detection Drone

> An autonomous UAV system powered by YOLOv8 for real-time fire and smoke detection.

---

## 📖 Overview

**Deadlock** is an intelligent drone project that integrates computer vision and deep learning to detect fire and smoke in real time. By mounting a YOLOv8 model on an autonomous UAV, the system can survey environments and flag hazards with minimal human intervention — making it suitable for wildfire monitoring, industrial inspection, and emergency response scenarios.

---

## ✨ Features

- 🔍 **Real-time detection** of fire and smoke using YOLOv8
- 🤖 **Autonomous UAV operation** with onboard inference
- 🎯 **Optimized model accuracy** through deep learning fine-tuning
- 📷 **Live video feed processing** via OpenCV
- 🧪 **Tested in controlled environments** for reliable performance

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLOv8 (Ultralytics) | Object detection model |
| OpenCV | Video capture & image processing |
| Jupyter Notebook | Model training & experimentation |
| Embedded Systems | UAV hardware integration |

---

## 📁 Project Structure

```
Deadlock/
├── Live.py                  # Real-time inference script for live drone feed
├── The_Notebook.ipynb       # Model training, evaluation & experiments
├── The_presentation.pptx    # Project presentation slides
├── Video Project 2.mp4      # Demo video
└── PFE si l'ingénieur Bilel Hamadi.pdf  # Full engineering report
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install ultralytics opencv-python
```

### Run Live Detection

```bash
python Live.py
```

This will activate the camera feed and begin real-time fire/smoke detection using the trained YOLOv8 model.

### Explore the Notebook

Open `The_Notebook.ipynb` in Jupyter to explore the full model training pipeline, dataset preparation, and evaluation metrics.

```bash
jupyter notebook The_Notebook.ipynb
```

---

## 📊 Model

The detection model is based on **YOLOv8**, fine-tuned on a fire and smoke dataset. Key improvements include:

- Custom dataset curation and augmentation
- Hyperparameter tuning for improved mAP
- Optimized for edge deployment on UAV hardware

---

## 📄 Report

A full engineering report is available in the repository: [`PFE si l'ingénieur Bilel Hamadi.pdf`](./PFE%20si%20l'ing%C3%A9nieur%20Bilel%20Hamadi.pdf)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

**Bilel Hamadi** — [@Crowley-source](https://github.com/Crowley-source)

---

## 📜 License

This project is open source. See the repository for details.
