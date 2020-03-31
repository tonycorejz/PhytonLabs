  
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
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
            print("Gender is %s" % (radioButton.gender))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())