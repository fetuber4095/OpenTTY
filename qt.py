

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.uic import loadUi

class OpenGUI(QFrame):
    def __init__(self):
        if ' '.join(sys.argv[1:]):
            super().__init__()
            loadUi(' '.join(sys.argv[1:]), self)

        else: print("qt: missing operand [ui.file]")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpenGUI()
    window.show()
    sys.exit(app.exec_())
