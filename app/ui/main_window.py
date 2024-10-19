from PyQt5.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QSlider, QMainWindow
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("AI-Powered Mood Tracker & Music Therapy")
        MainWindow.setGeometry(100, 100, 1000, 700)
        MainWindow.setWindowIcon(QIcon('icon.png'))  # Pastikan Anda memiliki ikon aplikasi

        # Mengatur palet warna utama
        palette = MainWindow.palette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        MainWindow.setPalette(palette)

        # Font kustom
        title_font = QFont("Helvetica Neue", 26, QFont.Bold)
        label_font = QFont("Helvetica Neue", 14)

        # Layout utama
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        # Label judul
        self.title_label = QLabel("AI-Powered Mood Tracker & Music Therapy", MainWindow)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                margin-bottom: 25px;
            }
        """)
        layout.addWidget(self.title_label)

        # Bagian tampilan kamera (placeholder)
        self.camera_label = QLabel("Kamera Akan Ditampilkan di Sini", MainWindow)
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setFixedSize(800, 400)
        self.camera_label.setStyleSheet("""
            QLabel {
                background-color: #ecf0f1;
                color: #7f8c8d;
                font-size: 18px;
                border: 2px dashed #bdc3c7;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.camera_label, alignment=Qt.AlignCenter)

        # Layout horizontal untuk tombol
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        self.detect_button = QPushButton("Mulai Deteksi Suasana Hati", MainWindow)
        self.detect_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                padding: 12px 20px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        button_layout.addWidget(self.detect_button)

        self.music_button = QPushButton("Atur Musik Terapi", MainWindow)
        self.music_button.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                font-size: 16px;
                padding: 12px 20px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)
        button_layout.addWidget(self.music_button)

        layout.addLayout(button_layout)

        # Slider volume
        self.volume_label = QLabel("Volume Musik Terapi", MainWindow)
        self.volume_label.setFont(label_font)
        self.volume_label.setAlignment(Qt.AlignCenter)
        self.volume_label.setStyleSheet("color: #34495e;")
        layout.addWidget(self.volume_label)

        self.volume_slider = QSlider(Qt.Horizontal, MainWindow)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 10px;
                background: #bdc3c7;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background-color: #3498db;
                border: 1px solid #2980b9;
                width: 22px;
                margin: -6px 0;
                border-radius: 11px;
            }
            QSlider::handle:horizontal:hover {
                background-color: #2980b9;
            }
        """)
        layout.addWidget(self.volume_slider)

        # Hasil deteksi
        self.result_label = QLabel("Hasil Deteksi Akan Ditampilkan di Sini", MainWindow)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(label_font)
        self.result_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #2c3e50;
                padding: 15px;
                border: 1px solid #bdc3c7;
                border-radius: 8px;
                background-color: #ecf0f1;
            }
        """)
        layout.addWidget(self.result_label)

        # Menetapkan layout ke central widget
        container = QWidget()
        container.setLayout(layout)
        MainWindow.setCentralWidget(container)
