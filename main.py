from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reslb = QtWidgets.QLabel(self.centralwidget)
        self.reslb.setGeometry(QtCore.QRect(10, 10, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.reslb.setFont(font)
        self.reslb.setFrameShape(QtWidgets.QFrame.Box)
        self.reslb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reslb.setLineWidth(2)
        self.reslb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reslb.setObjectName("reslb")
        self.btnmod = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("%"))
        self.btnmod.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnmod.setFont(font)
        self.btnmod.setObjectName("btnmod")
        self.btnc = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("C"))
        self.btnc.setGeometry(QtCore.QRect(120, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnc.setFont(font)
        self.btnc.setObjectName("btnc")
        self.btndivide = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("/"))
        self.btndivide.setGeometry(QtCore.QRect(320, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btndivide.setFont(font)
        self.btndivide.setObjectName("btndivide")
        self.btnarrow = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deleteBtn())
        self.btnarrow.setGeometry(QtCore.QRect(220, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnarrow.setFont(font)
        self.btnarrow.setObjectName("btnarrow")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("8"))
        self.btn8.setGeometry(QtCore.QRect(120, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btnmult = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.pressedBtn("x"))
        self.btnmult.setGeometry(QtCore.QRect(320, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnmult.setFont(font)
        self.btnmult.setObjectName("btnmult")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("7"))
        self.btn7.setGeometry(QtCore.QRect(10, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("9"))
        self.btn9.setGeometry(QtCore.QRect(220, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("5"))
        self.btn5.setGeometry(QtCore.QRect(120, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btnminus = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("-"))
        self.btnminus.setGeometry(QtCore.QRect(320, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnminus.setFont(font)
        self.btnminus.setObjectName("btnminus")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("4"))
        self.btn4.setGeometry(QtCore.QRect(10, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("6"))
        self.btn6.setGeometry(QtCore.QRect(220, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("2"))
        self.btn2.setGeometry(QtCore.QRect(120, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btnplus = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("+"))
        self.btnplus.setGeometry(QtCore.QRect(320, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnplus.setFont(font)
        self.btnplus.setObjectName("btnplus")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("1"))
        self.btn1.setGeometry(QtCore.QRect(10, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("3"))
        self.btn3.setGeometry(QtCore.QRect(220, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressedBtn("0"))
        self.btn0.setGeometry(QtCore.QRect(120, 490, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btneq = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.Calculate())
        self.btneq.setGeometry(QtCore.QRect(320, 490, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btneq.setFont(font)
        self.btneq.setObjectName("btneq")
        self.btninv = QtWidgets.QPushButton(self.centralwidget)
        self.btninv.setGeometry(QtCore.QRect(10, 490, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btninv.setFont(font)
        self.btninv.setObjectName("btninv")
        self.btndot = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.decimalClicked())
        self.btndot.setGeometry(QtCore.QRect(220, 490, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btndot.setFont(font)
        self.btndot.setObjectName("btndot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def pressedBtn(self,pressed):
        screen = self.reslb.text()
        if screen=="ERROR":
            self.reslb.setText("")
        if pressed == "C":
            self.reslb.setText("0")
        else:
            if self.reslb.text()=="0":
                self.reslb.setText("")
            self.reslb.setText(f'{self.reslb.text()}{pressed}')
    
    def Calculate(self):
        try:
            screen = self.reslb.text()
            screen =screen.replace("x","*")
            screen = eval(screen)
            self.reslb.setText(f'{str(screen)}')
        except:
            self.reslb.setText(f'ERROR')
    
    def decimalClicked(self):
        screen = self.reslb.text()
        if screen=="ERROR":
            self.reslb.setText("")
        if screen[-1]!=".":
            self.reslb.setText(f'{screen}.')
    
    def deleteBtn(self):
        screen=self.reslb.text()
        screen=screen[:-1]
        self.reslb.setText(f'{screen}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.reslb.setText(_translate("MainWindow", "0"))
        self.btnmod.setText(_translate("MainWindow", "%"))
        self.btnc.setText(_translate("MainWindow", "C"))
        self.btndivide.setText(_translate("MainWindow", "/"))
        self.btnarrow.setText(_translate("MainWindow", "Del"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnmult.setText(_translate("MainWindow", "X"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btnminus.setText(_translate("MainWindow", "-"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btnplus.setText(_translate("MainWindow", "+"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btneq.setText(_translate("MainWindow", "="))
        self.btninv.setText(_translate("MainWindow", "+/-"))
        self.btndot.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
