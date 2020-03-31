from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction
from PyQt5.QtCore import QSize
 
 

class MainWindow(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 320))    
        self.setWindowTitle("Коровин")  
        central_widget = QWidget(self)          
        self.setCentralWidget(central_widget)   
 
        grid_layout = QGridLayout(self)         
        central_widget.setLayout(grid_layout)          
 
        exit_action = QAction("&Exit", self)    
        exit_action.setShortcut('Ctrl+Q')       

        exit_action.triggered.connect(qApp.quit)

        file_menu = self.menuBar()
        file_menu.addAction(exit_action)
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())