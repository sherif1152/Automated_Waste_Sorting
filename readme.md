# Automated Waste Sorting System

This project implements an Automated Waste Sorting System utilizing computer vision and machine learning techniques to detect and sort `plastic`, `paper`, and `glass` materials. The system employs the YOLOv8 model for object detection.

## Working Mechanism

1. **Image Processing**: The system begins with image processing, where a camera captures images of the waste materials. These images are then sent to a Raspberry Pi for processing.

2. **Sorting Decision**: The Raspberry Pi processes the images and identifies the type of waste material (**plastic**, **paper**, **glass**). It then publishes the data to an Arduino Mega, which makes sorting decisions based on the received data.

3. **Actuator Action**: Upon receiving the sorting decision from the Raspberry Pi, the Arduino Mega triggers the pneumatic circuit. This circuit is responsible for pushing the waste product into the designated bin or moving it within the sorting mechanism for further processing.

## Requirements

- Python 3 or higher
- OpenCV (`pip install opencv-python`)
- Ultralytics YOLO (`pip install yolov8`)
- Serial library for Arduino communication (`pip install pyserial`)


## Components Used
- YOLOv8 model for for real-time object detection
- Camera for capturing images
- Raspberry Pi for image processing
- Arduino Mega for receiving sorting decisions and controlling actuators
- Pneumatic circuit for waste sorting

## Usage
To use the Automated Waste Sorting System:
1. Ensure all components are properly connected and powered.
2. Install the required libraries using pip.
3. Connect your webcam to your system.
4. Connect Arduino Mega to your system and replace `/dev/ttyACM0` with your Arduino's port in the script, and Upload  [this code](arduino_code/arduino_code.ino)
5. Place waste materials in front of the camera for sorting.

6. Run the script using Python:
    ```bash
    python sorting.py
    ```

![alt text](<Automated Waste Sorting System.png>)
