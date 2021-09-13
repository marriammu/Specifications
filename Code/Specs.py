
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import shutil
import os

class Ui_MainWindow():
    Codes=[]
    SearchedCodes=[]
    CheckBox=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1026, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        for i in range (1000):
            self.CheckBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
            font = QtGui.QFont()
            font.setFamily("Ubuntu Condensed")
            font.setPointSize(13)
            font.setBold(True)
            font.setItalic(True)
            font.setWeight(75)
            self.CheckBox[i].setFont(font)
            self.CheckBox[i].setObjectName("checkBox"+str(i))
            self.verticalLayout.addWidget(self.CheckBox[i])
            self.CheckBox[i].hide()
        
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda:self.Files()) 
        self.pushButton_3.clicked.connect(lambda:self.Edit())
        self.pushButton_2.clicked.connect(lambda:self.Exporting())
        

    
    def Files(self):
        self.inserted=self.lineEdit_5.text()
        _translate = QtCore.QCoreApplication.translate
        df = pd.read_excel(self.lineEdit.text())
        self.Codes=df.to_numpy()
        print(len(self.Codes))
        for i in range(len(self.SearchedCodes)):
            self.CheckBox[i].hide()
        self.SearchedCodes.clear()       
        for i in range (len(self.Codes)):
            if(len(self.inserted)!=0):
                if (self.Codes[i][0][0:len(self.inserted)]==self.inserted):
                    self.SearchedCodes.append(self.Codes[i][0])       
        for i in range(len(self.SearchedCodes)):
            self.CheckBox[i].show()
            self.CheckBox[i].setText(_translate("MainWindow", self.SearchedCodes[i]))

    def Edit(self):
        for i in range (len(self.SearchedCodes)):
            if  (self.CheckBox[i].isChecked()):
                if(os.path.exists(self.lineEdit_2.text()+"\\"+self.CheckBox[i].text()+'.doc')):
                    os.startfile(self.lineEdit_2.text()+"\\"+self.CheckBox[i].text()+'.doc')

    def Exporting(self):
        newpath = self.lineEdit_3.text()
        destination=[]
        if not os.path.exists(newpath+"\\"+self.lineEdit_4.text()):
            os.makedirs(newpath+"\\"+self.lineEdit_4.text())
        for i in range (len(self.SearchedCodes)):
            if  (self.CheckBox[i].isChecked()):
                shutil.copy(self.lineEdit_2.text()+"\\"+self.CheckBox[i].text()+'.pdf', self.lineEdit_3.text()+"\\"+self.lineEdit_4.text()+"\\"+self.CheckBox[i].text()+'.pdf')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Excel Path :"))
        self.label_2.setText(_translate("MainWindow", "Imported Files Path :"))
        self.label_4.setText(_translate("MainWindow", "Exported Files Path :"))
        self.label_3.setText(_translate("MainWindow", "Project Name :"))
        self.label_5.setText(_translate("MainWindow", "Code :"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit"))
        self.pushButton_2.setText(_translate("MainWindow", "Export"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())