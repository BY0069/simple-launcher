import os

from PyQt6.QtCore import pyqtSignal, QThread


class Threads(QThread):
    signal = pyqtSignal(bool)

    def __init__(self, args, parent=None):
        super(Threads, self).__init__(parent)
        self.args = args

    def run(self) -> None:
        os.system(".\\venv\\Scripts\\python.exe launch.py " + self.args)
        self.signal.emit(True)
