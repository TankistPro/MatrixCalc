# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.width = QtWidgets.QLineEdit(self.centralwidget)
        self.width.setGeometry(QtCore.QRect(110, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.width.setFont(font)
        self.width.setObjectName("width")
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(200, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 330, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(120, 380, 111, 41))
        self.nextBtn.setObjectName("nextBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 281, 20))
        self.label_5.setObjectName("label_5")
        self.opMatrixCb = QtWidgets.QCheckBox(self.centralwidget)
        self.opMatrixCb.setGeometry(QtCore.QRect(80, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.opMatrixCb.setFont(font)
        self.opMatrixCb.setObjectName("opMatrixCb")
        self.sumMatrixCB = QtWidgets.QCheckBox(self.centralwidget)
        self.sumMatrixCB.setGeometry(QtCore.QRect(120, 190, 111, 23))
        self.sumMatrixCB.setObjectName("sumMatrixCB")
        self.multMatrixCB = QtWidgets.QCheckBox(self.centralwidget)
        self.multMatrixCB.setGeometry(QtCore.QRect(120, 220, 111, 23))
        self.multMatrixCB.setObjectName("multMatrixCB")
        self.scalarMatrixCB = QtWidgets.QCheckBox(self.centralwidget)
        self.scalarMatrixCB.setGeometry(QtCore.QRect(80, 110, 181, 21))
        self.scalarMatrixCB.setObjectName("scalarMatrixCB")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.devMatrixCB = QtWidgets.QCheckBox(self.centralwidget)
        self.devMatrixCB.setGeometry(QtCore.QRect(120, 160, 111, 23))
        self.devMatrixCB.setObjectName("devMatrixCB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1) Определитель с одной матрицей"))
        self.label_2.setText(_translate("MainWindow", "x"))
        self.nextBtn.setText(_translate("MainWindow", "Далее"))
        self.label_3.setText(_translate("MainWindow", "2) Операции с несколькими матрицами"))
        self.label_4.setText(_translate("MainWindow", "Ввведите размерность матриц"))
        self.label_5.setText(_translate("MainWindow", "(Максимальный размер матрицы: 5 x 5)"))
        self.opMatrixCb.setText(_translate("MainWindow", "Поиск определителя"))
        self.sumMatrixCB.setText(_translate("MainWindow", "Сложение"))
        self.multMatrixCB.setText(_translate("MainWindow", "Умножение"))
        self.scalarMatrixCB.setText(_translate("MainWindow", "Умножение на сколяр"))
        self.label_6.setText(_translate("MainWindow", "Выберите действие  c матрицами(-ей):"))
        self.devMatrixCB.setText(_translate("MainWindow", "Вычитание"))
