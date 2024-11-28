import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt

class ParameterAdjuster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Frequency and Amplitude Adjuster')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Frequency: 1 Hz, Amplitude: 1', self)
        layout.addWidget(self.label)

        self.freq_slider = QSlider(Qt.Horizontal, self)
        self.freq_slider.setRange(1, 20)  # 주파수 범위
        self.freq_slider.setValue(1)
        self.freq_slider.valueChanged.connect(self.update_plot)
        layout.addWidget(self.freq_slider)

        self.amp_slider = QSlider(Qt.Horizontal, self)
        self.amp_slider.setRange(1, 10)  # 진폭 범위
        self.amp_slider.setValue(1)
        self.amp_slider.valueChanged.connect(self.update_plot)
        layout.addWidget(self.amp_slider)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.update_plot()

    def update_plot(self):
        freq = self.freq_slider.value()
        amp = self.amp_slider.value()
        self.label.setText(f'Frequency: {freq} Hz, Amplitude: {amp}')
        t = np.linspace(0, 1, 1000)
        y = amp * np.sin(2 * np.pi * freq * t)

        plt.clf()
        plt.plot(t, y)
        plt.title('Sine Wave')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.pause(0.01)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ParameterAdjuster()
    plt.ion()  # 실시간 플롯 활성화
    plt.show()
    sys.exit(app.exec_())
