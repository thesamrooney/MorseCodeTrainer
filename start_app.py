
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QTextBrowser, QPushButton, QSpinBox
from PyQt5 import uic

from morse.morse_generator import MorseGenerator
from trainer.training_generator import TrainingDataGenerator

from playsound import playsound

import sys
import os


class AppUI(QMainWindow):
    def __init__(self) -> None:
        super(AppUI, self).__init__()

        # load ui file
        uic.loadUi("app.ui", self)

        # create generators
        self.morse_gen = MorseGenerator()
        self.training_gen = TrainingDataGenerator()

        # Koch mode variables

        # Same word order as is used by lcwo.net
        # First level uses first 2 characters, each level beyond that adds 1
        self.koch_char_order = [
            "K", "M", "U", "R", "E", "S", "N", "A", "P", "T", "L", "W", "I", ".", 
            "J", "Z", "=", "F", "O", "Y", ",", "V", "G", "5", "/", "Q", "9", "2", 
            "H", "3", "8", "B", "?", "4", "7", "C", "1", "D", "6", "0", "X"
        ]

        # changing labels
        self.koch_label_grade_percent = self.findChild(QLabel, "kochGradePercent")
        self.koch_label_level_newchars = self.findChild(QLabel, "kochNewChars")

        # spins
        self.koch_spin_level = self.findChild(QSpinBox, "kochLevelSpin")
        self.koch_spin_char_wpm = self.findChild(QSpinBox, "kochCharWpmSpin")
        self.koch_spin_farn_wpm = self.findChild(QSpinBox, "kochFarnsworthWpmSpin")

        # buttons
        self.koch_btn_listen_newchars = self.findChild(QPushButton, "kochNewCharsListenBtn")
        self.koch_btn_listen_newchars.clicked.connect(self.koch_listen_newchars)

        self.koch_btn_listen_level = self.findChild(QPushButton, "kochStartLevelBtn")
        self.koch_btn_listen_level.clicked.connect(self.koch_listen_level)

        self.koch_btn_auto_grade = self.findChild(QPushButton, "kochAutoGradeBtn")
        self.koch_btn_auto_grade.clicked.connect(self.koch_auto_grade)

        # user decoded input
        self.koch_input_decoded = self.findChild(QPlainTextEdit, "decodedUserInput")

        # transmission output
        self.koch_output_decoded = self.findChild(QTextBrowser, "transmittedCharOutput")

        # runtime variables
        self.current_level_text = ""


        self.show()
    
    def get_all_level_chars(self) -> str:
        level = self.get_level()
        # maximum level is 40?
        allchars = self.koch_char_order[0:level+1]
        return "".join(allchars)
    
    def get_new_level_chars(self) -> str:
        level = self.get_level()
        if level == 1:
            return "".join(self.koch_char_order[:2])
        else:
            return self.koch_char_order[level+1]

    def get_level(self):
        return self.koch_spin_level.value()

    def koch_listen_newchars(self):
        message = ""
        new_chars = self.get_new_level_chars()
        print(new_chars)
        for char in str(new_chars):
            segment = ("" + char + " ") * 3
            message += segment
        print(message)
        morse = self.morse_gen.encode_morse(message)
        timing = self.morse_gen.generate_timing(morse)
        self.morse_gen.generate_audio(timing, "newchars.wav", wpm=18, farnsworth=15)
        playsound("newchars.wav", block=False) #TODO: replace this with a thread
        # os.remove("newchars.wav")

    def koch_listen_level(self):
        current_chars = self.get_all_level_chars()
        self.current_level_text = self.training_gen.random_chars(current_chars)
        morse = self.morse_gen.encode_morse(self.current_level_text)
        timing = self.morse_gen.generate_timing(morse)
        self.morse_gen.generate_audio(timing, "level.wav", wpm=18, farnsworth=15)
        playsound("level.wav", block=False) #TODO: replace this with a thread
        # os.remove("level.wav")

    def koch_auto_grade(self):
        #TODO: complete this method once auto-grading is available
        self.koch_output_decoded.clear()
        self.koch_output_decoded.append(self.current_level_text)



# init app

app = QApplication(sys.argv)
window = AppUI()

sys.exit(app.exec_())