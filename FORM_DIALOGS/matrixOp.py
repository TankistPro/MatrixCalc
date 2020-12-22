import sys
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt

from UI_PY.opMatrix import Ui_Dialog

# Открытие нового окна QDialog (Умножение на скаляр)
class matrixOp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, height=None, width=None):
        super(matrixOp, self).__init__(parent)

        #Отрисовка окна
        self.ui = Ui_Dialog()
        self.setupUi(self)
        self.initUI()

        # Установка размерности матрицы
        self.width = width
        self.height = height

        self.generateMatrix()

        # Нажатие на кнопку Умножить
        self.pushButton.clicked.connect(self.matrixOP)

    def initUI(self):
        self.setWindowTitle("Поиск определителя")
        # Фиксируем размер окна
        self.setFixedSize(self.geometry().width(), self.geometry().height())

    # Генерация пустой матрицы пользователя
    def generateMatrix(self):
        self.matrixArray = {}
        nameCounter = 0
        
        for h in range(self.height):
            for w in range(self.width):
                self.btn = QtWidgets.QLineEdit(self)
                self.btn.setFixedWidth(61)
                self.btn.setFixedHeight(31)
                
                self.gridLayout.addWidget(self.btn, h, w)

                self.matrixArray[nameCounter] = self.btn

                nameCounter += 1
        

    # Определитель матрицы
    def matrixOP(self):
        matrixString = ''
        count = 0
        for key in range(len(self.matrixArray)):
            if key == 0:
                matrixString += self.matrixArray[key].text()
            elif key == len(self.matrixArray) - 1:
                matrixString += " " + self.matrixArray[key].text()
                break
            else: 
                matrixString += " " + self.matrixArray[key].text()
            count += 1
            if count == self.width:
                matrixString += ";"
                count = 0

        self.detMatrix = round(np.linalg.det(np.matrix(matrixString)), 3)
        self.generateAnswer()

    # Генерация ответа 
    def generateAnswer(self):
        self.label_2.setText(str(self.detMatrix))
