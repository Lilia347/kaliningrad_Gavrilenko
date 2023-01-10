import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QDialog


class First_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('untitled1.ui', self)
        self.btnst.clicked.connect(self.open_Second_Window)

    def open_Second_Window(self):
        self.Second_Window = Second_Window(self)
        self.Second_Window.show()


class Second_Window(QDialog):
    def __init__(self, *arg):
        super().__init__()
        self.Third_Window = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Одежда по погоде')

        uic.loadUi('untitled2.ui', self)

        self.btn1.setStyleSheet('background-image: url(paint2.png)')
        self.btn2.setStyleSheet('background-image: url(paint3.jpg)')
        self.btn3.setStyleSheet('background-image: url(paint4.jpg)')
        self.btn4.setStyleSheet('background-image: url(paint5.png)')
        self.btn5.setStyleSheet('background-image: url(paint6.png)')
        self.btn6.setStyleSheet('background-image: url(paint7.png)')
        self.btn7.setStyleSheet('background-image: url(paint8.png)')
        self.btn8.setStyleSheet('background-image: url(paint9.png)')
        self.btn9.setStyleSheet('background-image: url(paint10.png)')

        self.btn19.clicked.connect(self.open_Third_Window)

    def open_Third_Window(self):
        print(1)
        self.Third_Window = Third_Window(self)
        print(2)
        self.Third_Window.show()
        print(3)


class Third_Window(QWidget):
    print(4)
    def __init__(self, *arg):
        print(5)
        super().__init__()
        print(6)
        self.initUI()
        print(7)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        print(9)
        self.setWindowTitle('Одежда по погоде')
        print(10)
        uic.loadUi('untitled3.ui', self)
        print(11)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = First_Window()
    ex.show()
    sys.exit(app.exec())