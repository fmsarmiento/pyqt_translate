# Import widgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QComboBox, QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # UI to be loaded
        uic.loadUi("translate.ui", self)
        self.setWindowTitle("Translate me now")
        # Define widgets here

        self.translate = self.findChild(QPushButton, "pushButton")
        self.clear = self.findChild(QPushButton, "pushButton_2")

        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox, "comboBox_2")

        self.text1 = self.findChild(QTextEdit, "textEdit")
        self.text2 = self.findChild(QTextEdit, "textEdit_2")

        # Define events here
        self.translate.clicked.connect(self.translate_fnx)
        self.clear.clicked.connect(self.clear_fnx)

        # Add the languages to the combo boxes
        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values()) # Conversion from dict to list (!) (!) (!) (!) (!)
        self.combo1.addItems(self.language_list)
        self.combo2.addItems(self.language_list)
        # Set default combo item
        self.combo1.setCurrentText("english")
        self.combo2.setCurrentText("filipino")
        # Show the app
        self.show()

    def translate_fnx(self):
        try: 
            for key, value in self.languages.items():
                if value == self.combo1.currentText():
                    fromKey = key
                if value == self.combo2.currentText():
                    toKey = key
            words = textblob.TextBlob(self.text1.toPlainText()) # Get text from text box, make it a textblob
            tmp = ""
            wpw = words.split(" ")
            for w in wpw:
                try:
                    w1 = w.translate(from_lang=fromKey, to=toKey)
                except Exception as e:
                    w1 = w
                tmp = tmp + " " + w1
            self.text2.setText(str(tmp[1:]))
        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))

    def clear_fnx(self):
        self.text1.setText("")
        self.text2.setText("")
        self.combo1.setCurrentText("english")
        self.combo2.setCurrentText("filipino")
    
# Initialisation
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()