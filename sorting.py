#!/usr/bin/env python3.8
import cv2
import argparse

from ultralytics import YOLO
import supervision as sv

import serial
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with your Arduino's port
last_command = None
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("yolov8n.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while True:
        ret, frame = cap.read()
        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )

        # Perform actions based on detections
        for _, confidence, class_id, _ in detections:
            label = model.model.names[class_id]
            
            if confidence > 0.7 and "bottle" in label.lower():
                        print("plastic")
                        command = 'P'
                        if command != last_command : 
                            arduino.write(command.encode())
                        

            if confidence > 0.7 and "cup" in label.lower():
                    print("Glass")
                    command = 'G'
                    if command != last_command : 
                        arduino.write(command.encode()) 

            if confidence > 0.7 and "book" in label.lower():
                    print("paper")
                    command = 'a'
                    if command != last_command : 
                        arduino.write(command.encode()) 
            if confidence > 0.7 and "donut" in label.lower():
                    print("paper")
                    command = 'P'
                    if command != last_command : 
                        arduino.write(command.encode())
        

        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break

if __name__ == "__main__":
    main()

