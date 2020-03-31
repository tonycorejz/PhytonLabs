import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
 
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("Вы нажали на кнопку")
        self.update()

    def initUI(self):
        self.setWindowTitle("Название программы")
        self.setGeometry(200, 200, 300, 300)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(100, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Кнопка")
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()