#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [qt.py]
#
#  This code is part of OpenTTY Package Repository
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


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
