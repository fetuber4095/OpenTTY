# This version of 'qt-runner.dll' is to native python 


global sys
global QApplication, QWidget, QFrame, loadUi

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.uic import loadUi

class OpenGUI(QFrame):
    def __init__(self):
        super().__init__()
        loadUi(' '.join(sys.argv[1:]), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpenGUI()
    window.show()
    sys.exit(app.exec_())
