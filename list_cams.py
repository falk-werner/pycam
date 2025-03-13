#!/usr/bin/env python3

import cv2

def main():
    print(f"ID\tWIDTH\tHEIGHT\tFPS")
    cv2.setLogLevel(0)
    for i in range(100):
        cam = cv2.VideoCapture(i)
        if cam.isOpened():
            width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cam.get(cv2.CAP_PROP_FPS))
            print(f"{i}\t{width}\t{height}\t{fps}")

if __name__ == "__main__":
    main()