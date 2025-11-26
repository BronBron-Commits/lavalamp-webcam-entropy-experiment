import cv2
import hashlib

class CameraEntropySource:
    def __init__(self, device_index=2, width=340, height=340):
        self.cap = cv2.VideoCapture(device_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'GREY'))

        if not self.cap.isOpened():
            raise RuntimeError("Camera failed to open")

    def get_entropy_chunk(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        data = frame.tobytes()
        return hashlib.sha256(data).digest()
