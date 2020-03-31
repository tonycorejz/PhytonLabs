﻿import sys 
from PyQt5 import QtCore, QtGui, QtWidgets 
  
class Ui_MainWindow(object): 
    def setupUi(self, MainWindow): 
        MainWindow.resize(476, 308) 
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
  
        # Languages are not selected initially hence initialised to zero. 
        self.langs ={'c':0, 'cpp':0, 'java':0, 'python':0} 
          
        # For showing message  
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(140, 80, 500, 20)) 
          
        self.checkBox_c = QtWidgets.QCheckBox(self.centralwidget) 
        self.checkBox_c.setGeometry(QtCore.QRect(170, 120, 100, 20)) 
        self.checkBox_c.stateChanged.connect(self.checkedc) 
          
        self.checkBox_cpp = QtWidgets.QCheckBox(self.centralwidget) 
        self.checkBox_cpp.setGeometry(QtCore.QRect(170, 140, 100, 20)) 
        self.checkBox_cpp.stateChanged.connect(self.checkedcpp) 
          
        self.checkBox_java = QtWidgets.QCheckBox(self.centralwidget) 
        self.checkBox_java.setGeometry(QtCore.QRect(170, 160, 100, 20)) 
        self.checkBox_java.stateChanged.connect(self.checkedjava) 
          
        self.checkBox_py = QtWidgets.QCheckBox(self.centralwidget) 
        self.checkBox_py.setGeometry(QtCore.QRect(170, 180, 100, 20)) 
        self.checkBox_py.stateChanged.connect(self.checkedpy) 
          
        MainWindow.setCentralWidget(self.centralwidget) 
  
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
          
    def checkedc(self, checked): 
        if checked: 
            self.langs['Acer Nitro']= 1
        else: 
            self.langs['Acer Nitro']= 0
        self.show() 
  
    def checkedcpp(self, checked): 
        if checked: 
            self.langs['BenQ']= 1
        else: 
            self.langs['BenQ']= 0    
        self.show() 
              
    def checkedjava(self, checked): 
        if checked: 
            self.langs['Dell']= 1
        else: 
            self.langs['Dell']= 0
        self.show() 
              
    def checkedpy(self, checked): 
        if checked: 
            self.langs['LG']= 1
        else: 
            self.langs['LG']= 0
        self.show()             
      
    # For showing updated list of all selected languages.          
    def show(self): 
        checkedlangs =', '.join([key for key in self.langs.keys() 
                                         if self.langs[key]== 1])  
          
        # Updates message having list of all selected languages.  
        self.label.setText("У вас есть "+checkedlangs) 
      
          
    def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate 
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) 
  
        self.label.setText(_translate("MainWindow", "Выберете мониторы, которые имеются в магазине")) 
        self.checkBox_c.setText(_translate("MainWindow", "Acer Nitro VG270UP")) 
        self.checkBox_cpp.setText(_translate("MainWindow", "BenQ PD2700U")) 
        self.checkBox_java.setText(_translate("MainWindow", "Dell U2718Q")) 
        self.checkBox_py.setText(_translate("MainWindow", "LG 27UK850W")) 
  
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)  
    
    MainWindow = QtWidgets.QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  
    sys.exit(app.exec_())  