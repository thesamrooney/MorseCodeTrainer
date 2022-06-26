
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import uic

import sys


class UI(QMainWindow):
    def __init__(self) -> None:
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("app.ui", self)

        self.show()


# init app

app = QApplication(sys.argv)
window = UI()

sys.exit(app.exec_())