

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.uic import loadUi

class OpenGUI(QFrame):
    def __init__(self):
        super().__init__()
        loadUi(' '.join(sys.argv[1:]), self)
        
if __name__ == "__main__": 
    if not ' '.join(sys.argv[1:]): print("qt: missing operand [ui.file]"), sys.exit()

    app = QApplication(sys.argv)
    window = OpenGUI()
    window.show()
    sys.exit(app.exec_())
