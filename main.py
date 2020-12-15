#pyuic5 form.ui -o ui.py -x
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout

from app import Ui_MainWindow
from firstNewWindow import Ui_Dialog

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
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

    def drowWindow(self):
        self.heightSize = int(self.height.text())
        self.widthSize = int(self.width.text())

        if self.heightSize <= 5 or self.heightSize <= 5:
            dialog = openNewWindow(self, self.heightSize, self.widthSize)
            dialog.exec_()
        else:
            print("Максимальная размерность матрицы 5x5!!!")

# Открытие нового окна QDialog
class openNewWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, height=None, width=None):
        super(openNewWindow, self).__init__(parent)

        #Отрисовка окна
        self.ui = Ui_Dialog()
        self.setupUi(self)
        self.initUI()

        # Установка размерности матрицы
        self.width = width
        self.height = height

        self.pushButton.clicked.connect(self.hel)

        self.generateMatrix()

    def initUI(self):
        self.setWindowTitle("Умножения на скаляр")
        # Фиксируем размер окна
        self.setFixedSize(self.geometry().width(), self.geometry().height())

    # Генерация пустой матрицы
    def generateMatrix(self):
        nameCounter = 0
        for h in range(self.height):
            for w in range(self.width):
                self.btn = QtWidgets.QLineEdit(self)
                self.btn.setFixedWidth(61)
                self.btn.setFixedHeight(31)
                self.btn.setObjectName(f"edit_{nameCounter}")
                
                self.gridLayout.addWidget(self.btn, h, w)

                nameCounter += 1
                print(self.btn)
    # Умножить
    def hel(self):
        print(self.edit_0.text())

# Экземпляр класса QApplication
app = QtWidgets.QApplication(sys.argv)
# Csоздание инстанса App
graphs = App()
# Запуск
sys.exit(app.exec_())