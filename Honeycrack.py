import random
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

def generate_data(process):
  """Generates a fake influx of continuous internet data using the specified process.

  Args:
    process: The process to use to generate the data. Valid values are 'random' and 'sequential'.

  Returns:
    A list of dictionaries, where each dictionary represents a piece of data.
  """
  if process == 'random':
    return generate_random_data()
  elif process == 'sequential':
    return generate_sequential_data()
  else:
    raise ValueError('Invalid process: {}'.format(process))

def generate_random_data():
  """Generates a fake influx of continuous internet data using a random process.

  Returns:
    A list of dictionaries, where each dictionary represents a piece of data.
  """
  data = []
  for i in range(1000):
    data.append({
      'timestamp': time.time(),
      'source_ip': random.randint(1, 255) * 256 * 256 + random.randint(1, 255) * 256 + random.randint(1, 255),
      'destination_ip': random.randint(1, 255) * 256 * 256 + random.randint(1, 255) * 256 + random.randint(1, 255),
      'port': random.randint(1, 65535),
      'protocol': random.choice(['TCP', 'UDP']),
      'bytes_sent': random.randint(1, 1000000),
      'bytes_received': random.randint(1, 1000000),
    })

  return data

def generate_sequential_data():
  """Generates a fake influx of continuous internet data using a sequential process.

  Returns:
    A list of dictionaries, where each dictionary represents a piece of data.
  """
  data = []
  for i in range(1000):
    data.append({
      'timestamp': time.time(),
      'source_ip': i,
      'destination_ip': i + 1,
      'port': i % 65535,
      'protocol': 'TCP' if i % 2 == 0 else 'UDP',
      'bytes_sent': i,
      'bytes_received': i,
    })

  return data

def main():
  app = QApplication([])

  window = QWidget()
  window.setWindowTitle('Fake Internet Data Generator')

  process_label = QLabel(window, text='Process:')
  process_combobox = QComboBox(window)
  process_combobox.addItems(['random', 'sequential'])

  honey_label = QLabel(window, text='Honey:')
  honey_input = QLineEdit(window)

  start_button = QPushButton(window, text='Start')
  start_button.clicked.connect(lambda: generate_data(process_combobox.currentText()))

  stop_button = QPushButton(window, text='Stop')
  stop_button.clicked.connect(window.close)

  weather_label = QLabel(window, text='Weather:')
  weather_widget = QWidget(window)
  weather_layout = QHBoxLayout(weather_widget)

  weather_icon = QLabel(weather_widget)
  weather_icon.setPixmap(QPixmap('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Weather_icon_-_sunny.svg/1200px-Weather_icon_-_sunny.svg.png'))

  weather_text = QLabel(weather_widget)
  weather_text.setText('Sunny')

  weather_layout.addWidget(weather_icon)
  weather_layout.addWidget(weather_text)


process_label.move(10, 10)
process_combobox.move(100, 10)
honey_label.move(10, 50)
honey_input.move(100, 50)
start_button.move(100, 100)
stop_button.move(200, 100)
weather_widget.move(300, 10)

window.show()

app.exec()

