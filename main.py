
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
import finder
import receiver
import imutils
import numpy as np

class NDIWindow(QMainWindow):
    def __init__(self, frame_width=750, frame_height=562, window_x=1700, window_y=960): # DONT CHANGE THIS, SEE BOTTOM OF FILE
        super().__init__()

        # Set dimensions
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.window_x = window_x
        self.window_y = window_y

        # Window settings
        self.setWindowTitle("NDI Monitor")
        self.setFixedSize(self.frame_width, self.frame_height)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Place window at specified coordinates
        self.move(self.window_x, self.window_y)

        # Label to display the NDI frame
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.frame_width, self.frame_height)

        # Initialize the NDI finder and receiver
        self.finder = finder.create_ndi_finder()
        self.sources = self.finder.get_sources()

        self.receiver = None
        if self.sources:
            self.setNDISource(0)  # Set the first available source by default

        # Timer for updating frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(0)  # ~30 FPS

    def setNDISource(self, index):
        self.receiver = receiver.create_receiver(self.sources[index])

    def update_frame(self):
        if self.receiver:
            try:
                frame = self.receiver.read()
                frame = imutils.resize(frame, width=self.frame_width)  # Resize to match window width
                b, g, r, a = frame.T  # Split channels
                frame = np.array([r, g, b, a]).transpose()  # Convert to RGBA format
                frame_data = frame.tobytes()  # Convert to bytes

                image = QImage(frame_data, frame.shape[1], frame.shape[0], frame.shape[1] * 4, QImage.Format_RGBA8888)
                pixmap = QPixmap.fromImage(image)
                self.label.setPixmap(pixmap)
            except Exception as e:
                print("Error receiving frame:", e)
                self.receiver = None  # Reset receiver if there's an error

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # CHANGE THIS
    x = 1700
    y = 960
    width = 750
    height = 562

    window = NDIWindow(frame_width=width, frame_height=height, window_x=x, window_y=y)
    window.show()
    sys.exit(app.exec_())
