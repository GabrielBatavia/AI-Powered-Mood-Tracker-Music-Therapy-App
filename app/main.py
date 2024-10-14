import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from backend.music_controller import MusicController
from backend.device_manager import DeviceManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup device manager untuk menghubungkan ke kamera
        self.device_manager = DeviceManager(self.ui.camera_label)
        self.device_manager.start_camera()

        # Setup music controller
        self.music_controller = MusicController()

        # Connect tombol dengan fungsi masing-masing
        self.ui.detect_button.clicked.connect(self.detect_mood)
        self.ui.music_button.clicked.connect(self.play_music)

    def detect_mood(self):
        self.ui.result_label.setText("Sedang menganalisis suasana hati... (dummy)")

    def play_music(self):
        self.music_controller.play_playlist('playlist1')  # Memutar playlist dummy

# Jalankan aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
