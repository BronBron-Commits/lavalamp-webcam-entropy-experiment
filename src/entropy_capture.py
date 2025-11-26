import cv2
import hashlib
import time

# Use /dev/video2 (GREY mode)
cap = cv2.VideoCapture(2)

# Force GREY 340x340
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 340)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 340)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'GREY'))

if not cap.isOpened():
    print("Camera failed to open.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame read error")
        continue

    # Frame is already greyscale in /dev/video2
    data = frame.tobytes()

    digest = hashlib.sha256(data).hexdigest()

    print("Entropy:", digest)

    time.sleep(0.5)
