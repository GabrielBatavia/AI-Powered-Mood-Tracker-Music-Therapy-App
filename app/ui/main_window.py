# from PyQt5.QtWidgets import (
#     QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QSlider, QMainWindow, QGraphicsDropShadowEffect
# )
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer, pyqtProperty
# from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QPainter, QTransform
# from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
#
# class AnimatedLabel(QLabel):
#     def __init__(self, text="", parent=None):
#         super().__init__(text, parent)
#         self._rotation = 0
#
#     def getRotation(self):
#         return self._rotation
#
#     def setRotation(self, rotation):
#         self._rotation = rotation
#         self.update()
#
#     rotation = pyqtProperty(float, fget=getRotation, fset=setRotation)
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         w = self.width()
#         h = self.height()
#         painter.translate(w / 2, h / 2)
#         painter.rotate(self._rotation)
#         painter.translate(-w / 2, -h / 2)
#         super().paintEvent(event)
#
# class Ui_MainWindow:
#     def setupUi(self, MainWindow):
#         MainWindow.setWindowTitle("AI-Powered Mood Tracker & Music Therapy")
#         MainWindow.setGeometry(100, 100, 1000, 700)
#         MainWindow.setWindowIcon(QIcon('icon.png'))  # Pastikan Anda memiliki ikon aplikasi
#
#         # Mengatur palet warna utama
#         palette = MainWindow.palette()
#         palette.setColor(QPalette.Window, QColor("#f5f7fa"))
#         MainWindow.setPalette(palette)
#
#         # Font kustom
#         title_font = QFont("Helvetica Neue", 28, QFont.Bold)
#         label_font = QFont("Helvetica Neue", 14)
#         button_font = QFont("Helvetica Neue", 16)
#
#         # Layout utama
#         layout = QVBoxLayout()
#         layout.setContentsMargins(40, 40, 40, 40)
#         layout.setSpacing(20)
#
#         # Label kamera (akan menampilkan feed kamera)
#         self.camera_label = QLabel(MainWindow)
#         self.camera_label.setAlignment(Qt.AlignCenter)
#         # Menyesuaikan ukuran untuk kamera laptop landscape
#         self.camera_label.setFixedSize(800, 450)
#         self.camera_label.setStyleSheet("""
#             QLabel {
#                 background-color: #ffffff;
#                 border: 1px solid #dcdde1;
#                 border-radius: 20px;
#             }
#         """)
#
#         # Label judul (dipindahkan ke atas kamera_label)
#         self.title_label = AnimatedLabel("AI-Powered Mood Tracker & Music Therapy", MainWindow)
#         self.title_label.setFont(title_font)
#         self.title_label.setAlignment(Qt.AlignCenter)
#         self.title_label.setStyleSheet("""
#             QLabel {
#                 color: #2c3e50;
#             }
#         """)
#
#         # Menambahkan efek bayangan pada judul
#         shadow_effect = QGraphicsDropShadowEffect()
#         shadow_effect.setBlurRadius(15)
#         shadow_effect.setOffset(0)
#         shadow_effect.setColor(QColor(0, 0, 0, 80))
#         self.title_label.setGraphicsEffect(shadow_effect)
#
#         # Menambahkan judul dan kamera_label ke layout vertikal
#         camera_layout = QVBoxLayout()
#         camera_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adds space above the title
#         camera_layout.addWidget(self.title_label)
#         camera_layout.addWidget(self.camera_label, alignment=Qt.AlignCenter)
#
#         # Membuat container widget untuk area kamera
#         camera_container = QWidget()
#         camera_container.setLayout(camera_layout)
#
#         layout.addWidget(camera_container)
#
#         # Animasi pada title_label
#         self.animate_title_label()
#
#         # Layout horizontal untuk tombol
#         button_layout = QHBoxLayout()
#         button_layout.setSpacing(30)
#         button_layout.setContentsMargins(0, 20, 0, 20)
#
#         self.detect_button = QPushButton("Mulai Deteksi Suasana Hati", MainWindow)
#         self.detect_button.setFont(button_font)
#         self.detect_button.setCursor(Qt.PointingHandCursor)
#         self.detect_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #1abc9c;
#                 color: white;
#                 padding: 15px 25px;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background-color: #16a085;
#             }
#         """)
#         button_layout.addWidget(self.detect_button)
#
#         self.music_button = QPushButton("Atur Musik Terapi", MainWindow)
#         self.music_button.setFont(button_font)
#         self.music_button.setCursor(Qt.PointingHandCursor)
#         self.music_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #3498db;
#                 color: white;
#                 padding: 15px 25px;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background-color: #2980b9;
#             }
#         """)
#         button_layout.addWidget(self.music_button)
#
#         layout.addLayout(button_layout)
#
#         # Slider volume dengan label
#         volume_layout = QHBoxLayout()
#         volume_layout.setSpacing(10)
#         volume_layout.setAlignment(Qt.AlignCenter)
#
#         self.volume_label = QLabel("Volume Musik Terapi", MainWindow)
#         self.volume_label.setFont(label_font)
#         self.volume_label.setStyleSheet("color: #34495e;")
#         volume_layout.addWidget(self.volume_label)
#
#         self.volume_slider = QSlider(Qt.Horizontal, MainWindow)
#         self.volume_slider.setRange(0, 100)
#         self.volume_slider.setValue(50)
#         self.volume_slider.setFixedWidth(300)
#         self.volume_slider.setStyleSheet("""
#             QSlider::groove:horizontal {
#                 height: 10px;
#                 background: #dcdde1;
#                 border-radius: 5px;
#             }
#             QSlider::handle:horizontal {
#                 background-color: #8e44ad;
#                 border: 1px solid #732d91;
#                 width: 22px;
#                 margin: -6px 0;
#                 border-radius: 11px;
#             }
#             QSlider::handle:horizontal:hover {
#                 background-color: #732d91;
#             }
#         """)
#         volume_layout.addWidget(self.volume_slider)
#
#         layout.addLayout(volume_layout)
#
#         # Hasil deteksi
#         self.result_label = QLabel("Hasil Deteksi Akan Ditampilkan di Sini", MainWindow)
#         self.result_label.setAlignment(Qt.AlignCenter)
#         self.result_label.setFont(label_font)
#         self.result_label.setFixedHeight(80)
#         self.result_label.setStyleSheet("""
#             QLabel {
#                 font-size: 16px;
#                 color: #2c3e50;
#                 padding: 20px;
#                 border: 1px solid #dcdde1;
#                 border-radius: 12px;
#                 background-color: #ffffff;
#             }
#         """)
#         result_shadow = QGraphicsDropShadowEffect()
#         result_shadow.setBlurRadius(10)
#         result_shadow.setOffset(0)
#         result_shadow.setColor(QColor(0, 0, 0, 50))
#         self.result_label.setGraphicsEffect(result_shadow)
#         layout.addWidget(self.result_label)
#
#         # Menetapkan layout ke central widget
#         container = QWidget()
#         container.setLayout(layout)
#         MainWindow.setCentralWidget(container)
#
#     def animate_title_label(self):
#         # Membuat animasi rotasi 3D pada label judul
#         self.title_animation = QPropertyAnimation(self.title_label, b"rotation")
#         self.title_animation.setDuration(4000)
#         self.title_animation.setStartValue(-5)
#         self.title_animation.setEndValue(5)
#         self.title_animation.setEasingCurve(QEasingCurve.InOutQuad)
#         self.title_animation.setLoopCount(-1)  # Ulangi terus menerus
#         self.title_animation.start()




# ui/main_window.py

import sys
import os
from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QPushButton, QSlider, QVBoxLayout,
    QWidget, QHBoxLayout, QGridLayout
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from plyer import notification


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        # Pengaturan utama window
        MainWindow.setWindowTitle("Mood Tracker")
        MainWindow.setWindowIcon(QIcon("ui/resources/icon.png"))
        MainWindow.resize(800, 600)

        # Central widget
        self.central_widget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.central_widget)

        # Layout utama
        main_layout = QVBoxLayout(self.central_widget)

        # Label untuk kamera
        self.camera_label = QLabel()
        self.camera_label.setPixmap(QPixmap("ui/resources/camera_placeholder.png"))
        self.camera_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.camera_label)

        # Label hasil analisis mood
        self.result_label = QLabel("Detected mood will appear here.")
        self.result_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.result_label)

        # Tombol kontrol
        self.detect_button = QPushButton("Detect Mood")
        self.music_button = QPushButton("Play Music")
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.detect_button)
        control_layout.addWidget(self.music_button)
        main_layout.addLayout(control_layout)

        # Slider volume
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        main_layout.addWidget(self.volume_slider)

        # Label notifikasi
        self.notification_label = QLabel("Welcome to Mood Tracker!")
        self.notification_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.notification_label)
