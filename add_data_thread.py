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
        self.list = []
        self.list_1 = ["data0", "data1", "data2", "data3", "data4"]

    def stop_thread(self):
        for i in range(self.count):
            self.thread[i].stop()

    def start_thread(self):
        self.count = int(self.uic.lineEdit.text())
        for i in range(self.count):
            self.thread[i] = multi_thread(index=i, data=self.list_1[i])
            self.thread[i].start()
            self.thread[i].signal.connect(self.receive_data)

    def receive_data(self, i, on_off, index):
        self.uic.tableWidget.setRowCount(self.count)
        self.uic.tableWidget.setItem(index, 0, QTableWidgetItem(str(i)))
        self.uic.tableWidget.setItem(index, 1, QTableWidgetItem(str(on_off)))
        self.uic.tableWidget.setItem(index, 2, QTableWidgetItem("thread: " + str(index)))


class multi_thread(QThread):
    signal = pyqtSignal(object, object, object)

    def __init__(self, index, data):
        super(multi_thread, self).__init__()
        self.random = None
        self.index = index
        self.data = data
        self.i = None
        self.on_off = "start"
        print("start thread", self.index, self.data)

    def run(self):
        self.on_off = "run"
        self.random = randint(0, 5)
        for self.i in range(self.random, 10):
            time.sleep(1)
            self.signal.emit(self.i, self.on_off, self.index)
        self.on_off = "stop"
        self.signal.emit(self.i, self.on_off, self.index)

    def stop(self):
        print("stop thread", self.index)
        self.on_off = "stop"
        self.signal.emit(self.i, self.on_off, self.index)
        self.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())