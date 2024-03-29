from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(140, 140, 140);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 440, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(255, 232, 57);")
        self.btn_0.setObjectName("btn_0")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 440, 150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 172, 56);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 100, 130))
        self.btn_7.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 50, 100, 130))
        self.btn_8.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 50, 100, 130))
        self.btn_9.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 180, 100, 130))
        self.btn_4.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 180, 100, 130))
        self.btn_5.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 180, 100, 130))
        self.btn_6.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 310, 100, 130))
        self.btn_1.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 310, 100, 130))
        self.btn_2.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 310, 100, 130))
        self.btn_3.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_3.setObjectName("btn_3")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 50, 100, 130))
        self.btn_minus.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 180, 100, 130))
        self.btn_plus.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(300, 310, 100, 130))
        self.btn_divide.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_multi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multi.setGeometry(QtCore.QRect(300, 440, 100, 60))
        self.btn_multi.setStyleSheet("background-color: rgb(255, 191, 42);")
        self.btn_multi.setObjectName("btn_multi")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_multi.setText(_translate("MainWindow", "*"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))
        self.btn_multi.clicked.connect(lambda: self.write_number(self.btn_multi.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, num):
        if self.label.text() == "0" or self.is_equal:
            self.label.setText(num)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + num)

    def results(self):
        if not self.is_equal:
            res = eval(self.label.text())
            self.label.setText(str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Error Window")
            error.setText("This action can not be acted")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
            error.setDefaultButton(QMessageBox.Cancel)

            error.setInformativeText("You can't press equal twice")
            error.setDetailedText("You pressed equal button twice")

            error.buttonClicked.connect(self.popup_action)
            error.exec_()

    def popup_action(self, btn):
        if btn.text() == "OK":
            print("Ok")

        elif btn.text() == "Reset":
            self.label.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
