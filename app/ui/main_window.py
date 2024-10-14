from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("AI-Powered Mood Tracker & Music Therapy")
        MainWindow.setGeometry(100, 100, 1000, 700)

        # Define main layout and appearance
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(25)

        # Define a sophisticated color scheme
        palette = MainWindow.palette()
        palette.setColor(QPalette.Background, QColor("#f0f2f5"))
        MainWindow.setPalette(palette)

        # Define a custom font for the title and labels
        title_font = QFont("Arial", 24, QFont.Bold)
        label_font = QFont("Arial", 14)

        # Title Label
        self.title_label = QLabel("AI-Powered Mood Tracker & Music Therapy", MainWindow)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #444444;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.title_label)

        # Camera display section (placeholder)
        self.camera_label = QLabel("Kamera Akan Ditampilkan di Sini", MainWindow)
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setFixedSize(800, 400)
        self.camera_label.setStyleSheet("""
            QLabel {
                background-color: #2d2d2d;
                color: #ffffff;
                font-size: 18px;
                border: 3px solid #888888;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.camera_label, alignment=Qt.AlignCenter)

        # Horizontal layout for buttons (deteksi suasana hati and music settings)
        button_layout = QHBoxLayout()

        self.detect_button = QPushButton("Mulai Deteksi Suasana Hati", MainWindow)
        self.detect_button.setStyleSheet("""
            QPushButton {
                background-color: #5c85d6;
                color: white;
                font-size: 18px;
                padding: 12px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #3b5998;
            }
        """)
        button_layout.addWidget(self.detect_button)

        self.music_button = QPushButton("Atur Musik Terapi", MainWindow)
        self.music_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 18px;
                padding: 12px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        button_layout.addWidget(self.music_button)

        layout.addLayout(button_layout)

        # Volume slider for music therapy control
        self.volume_label = QLabel("Volume Musik Terapi", MainWindow)
        self.volume_label.setFont(label_font)
        self.volume_label.setAlignment(Qt.AlignCenter)
        self.volume_label.setStyleSheet("color: #555555;")
        layout.addWidget(self.volume_label)

        self.volume_slider = QSlider(Qt.Horizontal, MainWindow)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 8px;
                background: #ddd;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background-color: #5c85d6;
                border: 1px solid #888;
                width: 20px;
                margin: -7px 0;
                border-radius: 10px;
            }
            QSlider::handle:horizontal:hover {
                background-color: #3b5998;
            }
        """)
        layout.addWidget(self.volume_slider)

        # Mood detection result display
        self.result_label = QLabel("Hasil Deteksi Akan Ditampilkan di Sini", MainWindow)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(label_font)
        self.result_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #333;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 8px;
                background-color: #f9f9f9;
            }
        """)
        layout.addWidget(self.result_label)

        # Set layout to central widget
        container = QWidget()
        container.setLayout(layout)
        MainWindow.setCentralWidget(container)
