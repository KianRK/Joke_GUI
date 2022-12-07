import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction
from Joke_backend import JokeBE

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.backend = JokeBE()

    def initializeUI(self):
        self.setGeometry(250, 250, 400, 300)
        self.setWindowTitle("Have a little laugh")
        self.setMinimumWidth(400)
        self.setMaximumWidth(500)
        
        self.setMinimumHeight(300)
        self.setMaximumHeight(450)

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        self.language_label = QLabel("In what language do you\nwant to laugh?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.language_label.setWordWrap(True)
        self.language_label.setFont(QFont("Noto Sans", 12))

        self.language_box = QComboBox()
        self.language_box.addItems(["German", "Englisch", "French"])
        self.language_box.setCurrentIndex(1)
        self.language_box.currentTextChanged.connect(self.setLanguage)
        self.language_box.setMaximumWidth(120)

        self.type_label = QLabel("What type of joke do you\nwant to hear?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.type_label.setWordWrap(True)
        self.type_label.setFont(QFont("Noto Sans", 12))

        self.type_box = QComboBox()
        self.type_box.addItems(["One liner", "Surprise", "Two liner"])
        self.type_box.setCurrentIndex(1)
        self.type_box.currentTextChanged.connect(self.setType)
        self.type_box.setMaximumWidth(120)

        self.joke_label = QLabel("", alignment = Qt.AlignmentFlag.AlignCenter)
        self.joke_label.setWordWrap(True)

        self.tellButton = QPushButton("Make me laugh!")
        self.tellButton.pressed.connect(self.printJoke)
        self.tellButton.setMaximumWidth(140)

        h_button_box = QHBoxLayout()
        h_button_box.addWidget(self.tellButton)
        h_button_box.setAlignment(Qt.AlignmentFlag.AlignCenter)

        h_language_box = QHBoxLayout()
        h_language_box.addWidget(self.language_label)
        h_language_box.addWidget(self.language_box)

        h_type_box = QHBoxLayout()
        h_type_box.addWidget(self.type_label)
        h_type_box.addWidget(self.type_box)

        v_box = QVBoxLayout()
        v_box.addLayout(h_language_box)
        v_box.addSpacing(15)
        v_box.addLayout(h_type_box)
        v_box.addLayout(h_button_box)
        v_box.addWidget(self.joke_label)

        container = QWidget()
        container.setLayout(v_box)
        self.setCentralWidget(container)

    def createActions(self):
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.save_joke = QAction("&Save Joke")
        self.save_joke.setShortcut("Ctrl+O")
        self.save_joke.triggered.connect(self.saveJoke)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)
        file_menu.addAction(self.save_joke)

    def saveJoke(self):
        file_name, ok = QFileDialog.getSaveFileName(self, "Open File", "/home/kian/Desktop/", "Text Files (*.txt)")


    def setLanguage(self):
        self.backend.joke_language = self.language_box.currentIndex()
        self.backend.setURl()

    def setType(self):
        self.backend.joke_type = self.type_box.currentIndex()
        self.backend.setURl()

    def printJoke(self):
        self.backend.setJokeText()
        self.joke_label.setText(self.backend.jokeText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())