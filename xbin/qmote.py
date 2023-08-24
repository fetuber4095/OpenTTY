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
