import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

from Form import Ui_launcher
from Threads import Threads


class MainWindow(QMainWindow, Ui_launcher):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.start)
        self.levels.buttonClicked.connect(self.setArgs)
        self.xformer.stateChanged.connect(self.enableXformers)
        self.deepdanbooru.stateChanged.connect(self.setDeepdanbooru)
        self.autolaunch.stateChanged.connect(self.setAutoLaunch)
        self.administrator.stateChanged.connect(self.setAdmin)

        self.argc = []
        self.args = ""

    def start(self):
        self.args = ' '.join(self.argc)
        self.thread = Threads(self.args)
        self.pushButton.setEnabled(False)
        self.pushButton.setText("启动中...")
        self.thread.signal.connect(self.update_button)
        self.thread.start()

    def update_button(self):
        self.pushButton.setEnabled(True)
        self.pushButton.setText("启动")

    def setArgs(self):
        sender = self.sender()
        if sender == self.levels:
            if self.levels.checkedId() == 1:
                if "--lowvram" in self.argc:
                    self.argc.remove("--lowvram")
                if "--medvram" in self.argc:
                    self.argc.remove("--medvram")
            elif self.levels.checkedId() == 2:
                if "--lowvram" in self.argc:
                    self.argc.remove("--lowvram")
                self.argc.append("--medvram")
            elif self.levels.checkedId() == 3:
                if "--medvram" in self.argc:
                    self.argc.remove("--medvram")
                self.argc.append("--lowvram")

    def enableXformers(self, state):
        if state == Qt.CheckState.Checked.value:
            self.argc.append("--xformers")
        else:
            self.argc.remove("--xformers")

    def setDeepdanbooru(self, state):
        if state == Qt.CheckState.Checked.value:
            self.argc.append("--deepdanbooru")
        else:
            self.argc.remove("--deepdanbooru")

    def setAutoLaunch(self, state):
        if state == Qt.CheckState.Checked.value:
            self.argc.append("--autolaunch")
        else:
            self.argc.remove("--autolaunch")

    def setAdmin(self, state):
        if state == Qt.CheckState.Checked.value:
            self.argc.append("--administrator")
        else:
            self.argc.remove("--administrator")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
