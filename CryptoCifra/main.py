# This Python file uses the following encoding: windows-1251
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget

import task1
import task2
import task3
import task4


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('CryptoCifra_V2.0')
        self.setFixedSize(1000, 550)

        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setText("CryptoCifra")
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setFont(QtGui.QFont('Arial', 35))
        self.lb1.setGeometry(350, 15, 300, 65)

        self.lb2 = QtWidgets.QLabel(self)
        self.lb2.setText("Криптографические методы")
        self.lb2.setFont(QtGui.QFont('Arial', 14))
        self.lb2.setGeometry(350, 70, 300, 50)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("RSA(number)")
        self.btn1.setFont(QtGui.QFont('Arial', 35))
        self.btn1.setGeometry(50, 150, 400, 100)
        self.btn1.clicked.connect(self.open_rsan_task)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("RSA(word)")
        self.btn2.setFont(QtGui.QFont('Arial', 35))
        self.btn2.setGeometry(50, 325, 400, 100)
        self.btn2.clicked.connect(self.open_rsaw_task)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("EDS(number)")
        self.btn3.setFont(QtGui.QFont('Arial', 35))
        self.btn3.setGeometry(550, 150, 400, 100)
        self.btn3.clicked.connect(self.open_edsn_task)

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText("EDS(word)")
        self.btn4.setFont(QtGui.QFont('Arial', 35))
        self.btn4.setGeometry(550, 325, 400, 100)
        self.btn4.clicked.connect(self.open_edsw_task)

    def open_rsan_task(self):
        task1.win1(self)


    def open_rsaw_task(self):
        task2.win2(self)

    def open_edsn_task(self):
        task3.win3(self)

    def open_edsw_task(self):
        task4.win4(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()