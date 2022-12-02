import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from Joke_backend import JokeBE
import urllib.request as ulib

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.backend = JokeBE()

    def initializeUI(self):
        self.setGeometry(250, 250, 350, 300)
        self.setWindowTitle("Have a little laugh")
        self.setMinimumWidth(300)
        
        self.setMinimumHeight(300)
        self.setMaximumHeight(600)

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.language_label = QLabel("In what language do you\nwant to laugh?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.language_label.setWordWrap(True)
        self.language_label.setFont(QFont("Noto Sans", 12))

        self.language_box = QComboBox()
        self.language_box.addItems(["German", "Englisch", "French"])
        self.language_box.currentTextChanged.connect(self.setLanguage)

        self.type_label = QLabel("What type of joke do you\nwant to hear?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.type_label.setWordWrap(True)
        self.type_label.setFont(QFont("Noto Sans", 12))

        self.type_box = QComboBox()
        self.type_box.addItems(["One liner", "Surprise", "Two liner"])
        self.type_box.currentTextChanged.connect(self.setType)

        self.joke_label = QLabel("", alignment = Qt.AlignmentFlag.AlignCenter)
        self.joke_label.setWordWrap(True)

        self.tellButton = QPushButton("Make me laugh!")
        self.tellButton.pressed.connect(self.printJoke)

        h_language_box = QHBoxLayout()
        h_language_box.addWidget(self.language_label)
        h_language_box.addWidget(self.language_box)

        h_type_box = QHBoxLayout()
        h_type_box.addWidget(self.type_label)
        h_type_box.addWidget(self.type_box)

        v_box = QVBoxLayout(self)
        v_box.addLayout(h_language_box)
        v_box.addLayout(h_type_box)
        v_box.addWidget(self.tellButton)
        v_box.addWidget(self.joke_label)

    def setLanguage(self):
        self.backend.joke_language = self.language_box.currentIndex()
        self.backend.setURl()
        print(self.language_box.currentIndex())
        print(self.backend.url)

    def setType(self):
        self.backend.joke_type = self.type_box.currentIndex()
        self.backend.setURl()
        print(self.type_box.currentIndex())
        print(self.backend.url)

    def printJoke(self):
        self.backend.setJokeText()
        self.joke_label.setText(self.backend.jokeText)
        
        print(self.backend.jokeText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())