#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [draw.py]
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QColorDialog, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = CanvasWidget(self)
        self.setCentralWidget(self.canvas)

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        new_action = QAction('New', self)
        new_action.triggered.connect(self.canvas.clear_canvas)
        file_menu.addAction(new_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_canvas)
        file_menu.addAction(save_action)

        color_menu = menubar.addMenu('Color')
        color_action = QAction('Choose Color', self)
        color_action.triggered.connect(self.choose_color)
        color_menu.addAction(color_action)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Qt-Draw')
        self.show()

    def save_canvas(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'PNG Files (*.png);;All Files (*)', options=options)
        if file_name:
            self.canvas.save_canvas(file_name)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color)

class CanvasWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.painting = False
        self.last_point = None
        self.pen = QPen(Qt.black, 2, Qt.SolidLine)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.painting = True

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.painting:
            painter = QPainter(self.image)
            painter.setPen(self.pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton and self.painting:
            self.painting = False

    def clear_canvas(self):
        self.image.fill(Qt.white)
        self.update()

    def set_pen_color(self, color):
        self.pen.setColor(color)

    def save_canvas(self, file_name):
        self.image.save(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint_app = PaintApp()
    sys.exit(app.exec_())
