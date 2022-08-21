# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
import time
from random import randint

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.tableWidget.setColumnWidth(0, 100)
        self.uic.tableWidget.setColumnWidth(2, 150)

        self.thread = {}
        self.uic.pushButton.clicked.connect(self.start_thread)
        self.uic.pushButton_2.clicked.connect(self.stop_thread)
        self.count = 0

    def stop_thread(self):
        for i in range(self.count):
            self.thread[i].stop()

    def start_thread(self):
        self.count = int(self.uic.lineEdit.text())
        for i in range(self.count):
            self.thread[i] = multi_thread(index=i)
            self.thread[i].start()
            self.thread[i].signal.connect(self.receive_data)

    def receive_data(self, data):
        self.uic.tableWidget.setRowCount(self.count)
        self.uic.tableWidget.setItem(data[2], 0, QTableWidgetItem(str(data[0])))
        self.uic.tableWidget.setItem(data[2], 1, QTableWidgetItem(str(data[1])))
        self.uic.tableWidget.setItem(data[2], 2, QTableWidgetItem("thread: " + str(data[2])))


class multi_thread(QThread):
    signal = pyqtSignal(object)

    def __init__(self, index):
        super(multi_thread, self).__init__()
        self.index = index
        self.io = None
        self.on_off = None
        self.i = None
        self.on_off = "start"
        print("start thread", self.index)

    def run(self):
        self.on_off = "run"
        self.io = randint(0, 5)
        for self.i in range(self.io, 50):
            time.sleep(1)
            data = [self.i, self.on_off, self.index]
            self.signal.emit(data)
        self.on_off = "stop"
        data = [self.i, self.on_off, self.index]
        self.signal.emit(data)

    def stop(self):
        self.terminate()
        print("stop thread", self.index)
        self.on_off = "stop"
        data = [self.i, self.on_off, self.index]
        self.signal.emit(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())