import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from plyer import notification
from ui.main_window import Ui_MainWindow
from backend.music_controller import MusicController
from backend.device_manager import DeviceManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Apply stylesheet
        with open("ui/styles/main.qss", "r") as style_file:
            self.setStyleSheet(style_file.read())

        # Setup device manager untuk menghubungkan ke kamera
        self.device_manager = DeviceManager(self.ui.camera_label)
        self.device_manager.start_camera()

        # Setup music controller
        self.music_controller = MusicController()

        # Connect tombol dengan fungsi masing-masing
        self.ui.detect_button.clicked.connect(self.detect_mood)
        self.ui.music_button.clicked.connect(self.play_music)

        # Connect slider volume ke backend
        self.ui.volume_slider.valueChanged.connect(self.update_volume)

        # Timer untuk notifikasi
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_notification)
        self.timer.start(10000)  # Notifikasi setiap 10 detik

        # Kirim notifikasi langsung saat app dijalankan
        self.send_notification()

    def detect_mood(self):
        # Placeholder fungsi deteksi mood
        mood = "Happy"  # Dummy data
        self.ui.result_label.setText(f"Detected Mood: {mood}")
        self.ui.notification_label.setText("Mood detected successfully.")

    def play_music(self):
        # Memutar musik dari playlist
        self.music_controller.play_playlist('playlist1')  # Ganti sesuai kebutuhan backend
        self.ui.notification_label.setText("Playing music...")

    def update_volume(self):
        # Update volume berdasarkan slider
        volume = self.ui.volume_slider.value()
        self.music_controller.set_volume(volume / 100)  # Volume dalam range 0-1
        self.ui.notification_label.setText(f"Volume set to {volume}%")

    def send_notification(self):
        try:
            notification.notify(
                title="Mood Tracker",
                message="Don't forget to relax and check your mood!",
                app_name="Mood Tracker",
                timeout=5
            )
            self.ui.notification_label.setText("Desktop notification sent.")
        except Exception as e:
            print(f"Failed to send notification: {e}")

    def closeEvent(self, event):
        # Bersihkan sumber daya sebelum aplikasi ditutup
        self.device_manager.stop_camera()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ui/resources/icon.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
