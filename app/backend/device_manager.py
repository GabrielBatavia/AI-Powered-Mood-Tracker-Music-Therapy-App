import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

class DeviceManager:
    def __init__(self, camera_label):
        self.camera_label = camera_label
        self.cap = cv2.VideoCapture(0)  # Buka kamera device

        # Buat timer untuk update frame kamera setiap 30 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def start_camera(self):
        self.timer.start(30)  # Mulai timer untuk update frame

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.camera_label.setPixmap(pixmap)

    def stop_camera(self):
        self.timer.stop()
        self.cap.release()
