import sys 
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def initUI(self):
        self.setWindowTitle("Название программы")
        self.setGeometry(200, 200, 300, 300)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(100, 100)

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.initUI()
        self.setLayout(layout)

        radiobutton = QRadioButton("Male")
        radiobutton.setChecked(True)
        radiobutton.gender = "Male"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Male")
        radiobutton.gender = "Female"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label.setText("Gender is %s" %radioButton.gender)
            

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())