import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QPushButton, QWidget


class myApplication(QWidget):
    def __init__(self):
        super(myApplication, self).__init__()

        self.pixmap = QtGui.QPixmap("steering-wheel.png")

        self.label = QLabel(self)
        self.label.setMinimumSize(600, 600)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(self.pixmap)

        grid = QGridLayout()

        button = QPushButton('Rotate 15 degrees')
        button.clicked.connect(self.rotate_pixmap)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(button, 1, 0)

        self.setLayout(grid)

        self.rotation = 0

    def rotate_pixmap(self):
        pixmap_1 = QtGui.QPixmap(self.pixmap)
        pixmap = pixmap_1.copy()
        self.rotation += 15
        transform = QtGui.QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myApplication()
    w.show()
    sys.exit(app.exec_())