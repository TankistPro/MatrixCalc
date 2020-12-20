import sys

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
        self.pushButton.clicked.connect(self.scalarMult)

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
        

    # Умножиение на скаляр
    def scalarMult(self):
        self.answerArray = []
        try:
            scalarNum = int(self.lineEdit.text())
        except ValueError:
            print ("Некорректне значение!")
        
        #print(len(self.matrixArray))
        for key in range(len(self.matrixArray)):
            valueMatrix = int(self.matrixArray[key].text())
            self.answerArray.append(valueMatrix * scalarNum)

        self.generateAnswer()

    # Генерация ответа 
    def generateAnswer(self):
        self.countAnswer = 0
        for h in range(self.height):
            for w in range(self.width):
                answerLabel = QtWidgets.QLabel(str(self.answerArray[self.countAnswer]))
                answerLabel.setAlignment(Qt.AlignCenter)
                self.answerGridLayout.addWidget(answerLabel, h, w)
                self.countAnswer += 1
