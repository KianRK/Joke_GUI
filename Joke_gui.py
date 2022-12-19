import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction
from Joke_backend import JokeBE

style_sheet = """

    QWidget{
        font-family: helvetica
    }

    QLabel#Description_Label{
        background-color: skyblue;
        color: black;
        border-radius: 5px;
        border-width: 3px;
    }
"""

#our class inherits from QMainWindow, since it has methods for creating,
#menus and toolbars
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        #Creating an instance of JokeBE, which is our applications backend
        self.backend = JokeBE()

    def initializeUI(self):
        self.setGeometry(250, 250, 400, 300)
        self.setWindowTitle("Have a little laugh")
        self.setMinimumWidth(400)
        self.setMaximumWidth(500)
        
        self.setMinimumHeight(300)
        self.setMaximumHeight(450)
        #below we execute self defined methods that get implemented further below.
        #Since they are called inside initializeUI, which by itself is called in __init__,
        #all these methods get executed once we create a MainWindow instance.
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()

        #A built in method of QMainWindow to display the window on screen.
        self.show()

    #In this meth
    def setUpMainWindow(self):

        #These next lines create the individual elements resp. the widgets that are nested inside our Main Window
        #First we create a text label as a QLabel instance to give the user the instruction choose a joke language.
        self.language_label = QLabel("In what language do you\nwant to laugh?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.language_label.setObjectName("Description_Label")
        self.language_label.setWordWrap(True)
        self.language_label.setFont(QFont("Noto Sans", 12))

        #Creating a dropdown menu as a QComboBox instance and adding the choosable languages with
        #the addItems method.
        self.language_box = QComboBox()
        self.language_box.addItems(["German", "Englisch", "French"])
        #Setting the current index to 1 resp. "Englisch", since that is the default setting
        #for the url that is requestion from the jokeapi website
        self.language_box.setCurrentIndex(1)
        #Connecting the Widget with the setLanguage method so that each time the choosen language
        #is changed, the joke_language attribute and the url attribute of the backend instance gets updated
        self.language_box.currentTextChanged.connect(self.setLanguage)
        self.language_box.setMaximumWidth(120)

        #Creating a text label as a QLabel instance to give the user the instruction choose a joke type.
        self.type_label = QLabel("What type of joke do you\nwant to hear?\t", alignment = Qt.AlignmentFlag.AlignLeft)
        self.type_label.setObjectName("Description_Label")
        self.type_label.setWordWrap(True)
        self.type_label.setFont(QFont("Noto Sans", 12))

        #Functionality analog to self.language box only that languages are replaced with joke types
        self.type_box = QComboBox()
        self.type_box.addItems(["One liner", "Surprise", "Two liner"])
        self.type_box.setCurrentIndex(1)
        self.type_box.currentTextChanged.connect(self.setType)
        self.type_box.setMaximumWidth(120)

        #A QLabel instance, created empty, in which the joke text will later be displayed.
        self.joke_label = QLabel("", alignment = Qt.AlignmentFlag.AlignCenter)
        self.joke_label.setWordWrap(True)

        #Creating a QPushButton instance with wich the user can request a joke with the
        #set parameters.
        self.tellButton = QPushButton("Make me laugh!")
        #Connencting the button with the printJoke method of the backend instance, that sets the joke
        #text inside the joke_label widget.
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
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    sys.exit(app.exec())