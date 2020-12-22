import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt

from UI_PY.multMatrix import Ui_Dialog

class matrixMult(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, height=None, width=None):
        super(matrixMult, self).__init__(parent)

        #Отрисовка окна
        self.ui = Ui_Dialog()
        self.setupUi(self)
        self.initUI()

        # Установка размерности матрицы
        self.width = width
        self.height = height

        self.generateMatrix()

        # Нажатие на кнопку Умножить
        self.pushButton.clicked.connect(self.multMatrix)

    def initUI(self):
        self.setWindowTitle("Умножение")
        # Фиксируем размер окна
        self.setFixedSize(self.geometry().width(), self.geometry().height())

    # Генерация пустой матрицы пользователя
    def generateMatrix(self):
        self.matrixArray_1 = {}
        self.matrixArray_2 = {}

        nameCounter_1 = 0
        # Генерация первой матрицы
        for h in range(self.height):
            for w in range(self.width):
                self.btn = QtWidgets.QLineEdit(self)
                self.btn.setFixedWidth(61)
                self.btn.setFixedHeight(31)
                
                self.gridLayout.addWidget(self.btn, h, w)
                self.matrixArray_1[nameCounter_1] = self.btn

                nameCounter_1 += 1
        
        nameCounter_2 = 0
        # Генерация Второй матрицы
        for h in range(self.height):
            for w in range(self.width):
                self.btn_2 = QtWidgets.QLineEdit(self)
                self.btn_2.setFixedWidth(61)
                self.btn_2.setFixedHeight(31)
                
                self.gridLayout_2.addWidget(self.btn_2, h, w)
                self.matrixArray_2[nameCounter_2] = self.btn_2

                nameCounter_2 += 1

    # Умножиение
    def multMatrix(self):
        self.answerArray = []
        
        #print(len(self.matrixArray))
        for key in range(len(self.matrixArray_1)):
            valueMatrix_1 = int(self.matrixArray_1[key].text())
            valueMatrix_2 = int(self.matrixArray_2[key].text())
            self.answerArray.append(valueMatrix_1 * valueMatrix_2)

        self.generateAnswer()

    # Генерация ответа 
    def generateAnswer(self):
        self.countAnswer = 0
        for h in range(self.height):
            for w in range(self.width):
                answerLabel = QtWidgets.QLabel(str(self.answerArray[self.countAnswer]))
                answerLabel.setAlignment(Qt.AlignCenter)
                self.gridLayout_3.addWidget(answerLabel, h, w)
                self.countAnswer += 1

