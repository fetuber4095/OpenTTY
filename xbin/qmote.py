#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [pname.py]
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PhotoViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('(OpenTTY) QMote')

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_image)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(open_action)

        self.setGeometry(100, 100, 800, 600)

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)', options=options)
        
        if file_name:
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = PhotoViewer()
    viewer.show()
    sys.exit(app.exec_())
