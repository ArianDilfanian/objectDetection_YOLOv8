# Object Tracking with YOLOv8

This repository demonstrates real-time object tracking using the YOLOv8 model and OpenCV. The implementation is designed to process video frames, detect and track objects, and visualize the results in a user-friendly interface.

## Project Overview
The primary goal of this project is to showcase the capabilities of YOLOv8 for object detection and tracking. The project reads frames from a video file, applies YOLOv8 to detect objects, and tracks them persistently across frames, providing a seamless visualization of the tracking process.

## Features
- **Real-Time Object Tracking**: Implements YOLOv8 for detecting and tracking objects in video frames.
- **Customizable Visualization**: Resizable OpenCV window for better visualization.
- **Interactive Control**: Press 'q' to stop the video processing at any time.

## Repository Contents
- **`main.py`**: Python script for object tracking using YOLOv8 and OpenCV.
- **`cars.mp4`**: Example video file used for object tracking (replace with your own video).
- **`requirements.txt`**: List of required Python libraries.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ArianDilfanian/YOLOv8-Object-Tracking.git
   cd YOLOv8-Object-Tracking
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the YOLOv8 model weights:
   - Download the pre-trained YOLOv8 weights (`yolov8n.pt`) from the [Ultralytics repository](https://github.com/ultralytics/ultralytics) or replace with your custom-trained weights.

## Usage
1. Run the Python script:
   ```bash
   python main.py
   ```

2. The script will process the video specified in `video_path` (default: `cars.mp4`). Replace `video_path` with the path to your own video if needed.

3. A window will display the processed video with detected and tracked objects.
   - Press **'q'** to exit the visualization.

## Code Explanation
The core implementation involves:
- Initializing the YOLOv8 model using `ultralytics`.
- Reading frames from the video file using OpenCV.
- Detecting and tracking objects with `model.track`.
- Plotting and visualizing the tracking results in real-time.

## Customization
- **Model Weights**: Replace `yolov8n.pt` with any other YOLOv8 model weights.
- **Video Source**: Change `video_path` to use a different video file.
- **Visualization Settings**: Modify the OpenCV window size or layout to suit your display.

## Dependencies
- Python 3.8+
- OpenCV
- Ultralytics

Install these using:
```bash
pip install opencv-python ultralytics
```



## Acknowledgments
- [Ultralytics](https://github.com/ultralytics) for the YOLOv8 model.
- [OpenCV](https://opencv.org/) for computer vision tools.


## Video



https://github.com/user-attachments/assets/7ed0cf02-942a-4f53-9132-326f9c84676f




