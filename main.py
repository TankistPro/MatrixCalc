#pyuic5 form.ui -o ui.py -x
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt

from UI_PY.app import Ui_MainWindow

from FORM_DIALOGS.matrixScalar import openNewWindow
from FORM_DIALOGS.matrixMult import matrixMult
from FORM_DIALOGS.matrixSum import matrixSum
from FORM_DIALOGS.matrixDev import matrixDev
from FORM_DIALOGS.matrixOp import matrixOp

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.mathOperation = ""
        self.initUI()
        self.btnClick()

    def initUI(self):
        self.setWindowTitle("Matrix calculator")
        # Создание формы и Ui
        self.setupUi(self)
        # Фиксируем размер окна
        self.setFixedSize(self.geometry().width(), self.geometry().height())
        # Показывает наше окно
        self.show()

    def btnClick(self):
        # Кнопка "Далее"
        self.nextBtn.clicked.connect(self.drowWindow)

    # Определение выбранной математической операции
    def checkOperation(self):
        checkBoxs = {
            "sum" : self.sumMatrixCB,
            "dev" : self.devMatrixCB,
            "mult" : self.multMatrixCB,
            "op" : self.opMatrixCb,
            "scalar" : self.scalarMatrixCB
        }
        mathOperationDialogs = { 
            "mult" : matrixMult, 
            "sum": matrixSum, 
            "dev": matrixDev,
            "scalar": openNewWindow,
            "op": matrixOp
        }

        for key in checkBoxs.keys():
            if checkBoxs[key].isChecked():
                for dialog in mathOperationDialogs.keys():
                    if dialog == key:
                        return mathOperationDialogs[dialog]

    def drowWindow(self):
        operation = self.checkOperation()
        try:
            self.heightSize = int(self.height.text())
            self.widthSize = int(self.width.text())

            if self.heightSize <= 5 or self.heightSize <= 5:
                dialog = operation(self, self.heightSize, self.widthSize)
                dialog.exec_()
            else:
                print("Максимальная размерность матрицы 5x5!!!")
        except ValueError:
            print("Некорректне значение!")
                        

# Экземпляр класса QApplication
app = QtWidgets.QApplication(sys.argv)
# Csоздание инстанса App
graphs = App()
# Запуск
sys.exit(app.exec_())