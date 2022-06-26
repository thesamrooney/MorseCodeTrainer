
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QTextBrowser, QPushButton, QSpinBox
from PyQt5 import uic

import sys


class UI(QMainWindow):
    def __init__(self) -> None:
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("app.ui", self)

        # get Koch Mode widgets

        # changing labels
        self.koch_label_grade_percent = self.findChild(QLabel, "kochGradePercent")
        self.koch_label_level_newchars = self.findChild(QLabel, "kochNewChars")

        # spins
        self.koch_spin_level = self.findChild(QSpinBox, "kochLevelSpin")
        self.koch_spin_char_wpm = self.findChild(QSpinBox, "kochCharWpmSpin")
        self.koch_spin_farn_wpm = self.findChild(QSpinBox, "kochFarnsworthWpmSpin")

        # buttons
        self.koch_btn_listen_newchars = self.findChild(QPushButton, "kochNewCharsListenBtn")
        self.koch_btn_listen_level = self.findChild(QPushButton, "kochStartLevelBtn")
        self.koch_btn_auto_grade = self.findChild(QPushButton, "kochAutoGradeBtn")

        # user decoded input
        self.koch_input_decoded = self.findChild(QPlainTextEdit, "decodedUserInput")

        # transmission output
        self.koch_output_decoded = self.findChild(QTextBrowser, "transmittedCharOutput")


        self.show()


# init app

app = QApplication(sys.argv)
window = UI()

sys.exit(app.exec_())