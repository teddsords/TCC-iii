from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.registerPerson_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerPerson_pushButton.setGeometry(QtCore.QRect(380, 270, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.registerPerson_pushButton.setFont(font)
        self.registerPerson_pushButton.setAutoDefault(False)
        self.registerPerson_pushButton.setDefault(False)
        self.registerPerson_pushButton.setFlat(False)
        self.registerPerson_pushButton.setObjectName("registerPerson_pushButton")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 70, 971, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.classify_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.classify_pushButton.setGeometry(QtCore.QRect(380, 360, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.classify_pushButton.setFont(font)
        self.classify_pushButton.setAutoDefault(False)
        self.classify_pushButton.setDefault(False)
        self.classify_pushButton.setFlat(False)
        self.classify_pushButton.setObjectName("classify_pushButton")
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setGeometry(QtCore.QRect(880, 650, 91, 20))
        self.text_label.setObjectName("text_label")
        self.myName_label = QtWidgets.QLabel(self.centralwidget)
        self.myName_label.setGeometry(QtCore.QRect(880, 670, 91, 20))
        self.myName_label.setObjectName("myName_label")
        self.credits_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.credits_pushButton.setGeometry(QtCore.QRect(380, 450, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.credits_pushButton.setFont(font)
        self.credits_pushButton.setAutoDefault(False)
        self.credits_pushButton.setDefault(False)
        self.credits_pushButton.setFlat(False)
        self.credits_pushButton.setObjectName("credits_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 260, 221, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Robot cartoon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 270, 251, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Elderly falling 4.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerPerson_pushButton.setText(_translate("MainWindow", "Register contact"))
        self.title_label.setText(_translate("MainWindow", "Fall Alert"))
        self.classify_pushButton.setText(_translate("MainWindow", "Classify data"))
        self.text_label.setText(_translate("MainWindow", "App developed by:"))
        self.myName_label.setText(_translate("MainWindow", "Teddy Ordoñez"))
        self.credits_pushButton.setText(_translate("MainWindow", "Credits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
