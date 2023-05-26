import random
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import psutil


app = QApplication([])

def generate_data(process):
    proc = psutil.Process(process.pid)
    conns = proc.connections()
    return [{
        'timestamp': time.time(),
        'source_ip': conn.laddr[0],
        'destination_ip': conn.raddr[0],
        'port': conn.laddr[1],
        'protocol': conn.type,
        'bytes_sent': random.randint(1, 1000000),
        'bytes_received': random.randint(1, 1000000)
    } for conn in conns]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(600, 400)
        self.move(250, 150)

        layout = QVBoxLayout()

        process_label = QLabel(self, text='Process:')
        self.process_combobox = QComboBox(self)
        for proc in psutil.process_iter():
            self.process_combobox.addItem(proc.name())

        self.timer_label = QLabel(self, text='Time left: 3 days')

        start_button = QPushButton(self, text='Start')
        stop_button = QPushButton(self, text='Stop')

        start_button.clicked.connect(self.start_timer)
        stop_button.clicked.connect(self.stop_timer)

        weather_widget = QWidget(self)
        weather_layout = QHBoxLayout(weather_widget)

        weather_icon = QLabel(weather_widget)
        weather_icon.setPixmap(QPixmap('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Weather_icon_-_sunny.svg/1200px-Weather_icon_-_sunny.svg.png'))

        weather_text = QLabel(weather_widget)
        weather_text.setText('Sunny')

        weather_layout.addWidget(weather_icon)
        weather_layout.addWidget(weather_text)

        layout.addWidget(process_label)
        layout.addWidget(self.process_combobox)
        layout.addWidget(self.timer_label)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)
        layout.addWidget(weather_widget)

        self.setLayout(layout)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 3 * 24 * 60 * 60  # 3 days timer

    def start_timer(self):
        self.timer.start(1000)  # Update every second

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        self.time_left -= 1

        if self.time_left == 0:
            self.timer.stop()

        days = self.time_left // (24 * 60 * 60)
        self.timer_label.setText(f'Time left: {days} days')


def main():
    window = MainWindow()
    window.show()

    app.exec()


main()