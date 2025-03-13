#!/usr/bin/env python3

import argparse
import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--camera", type=int, default=0)
    parser.add_argument("-x", "--width", type=int, default=640)
    parser.add_argument("-y","--height", type=int, default=480)
    parser.add_argument("-t", "--title", type=str, default="PyCam")
    args = parser.parse_args()
    camera_id = args.camera
    width = args.width
    height = args.height
    title = args.title

    cap = cv2.VideoCapture(camera_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    root = tk.Tk()
    root.title(title)
    label = ttk.Label(root)
    label.pack(fill=tk.BOTH,expand=True)
    def next_frame():
        _, frame = cap.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label.photo_image = photo_image
        label.configure(image=photo_image)
        label.after(10, next_frame)
    next_frame()
    root.geometry(f"{width}x{height}")
    root.attributes('-topmost', True)
    root.mainloop()

if __name__ == "__main__":
    main()
