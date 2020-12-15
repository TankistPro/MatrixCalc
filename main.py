import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from app import Ui_MainWindow

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()
        self.btnClick()

    def initUI(self):
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

# Открытие нового окна
class openNewWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, height=None, width=None):
        super(openNewWindow, self).__init__(parent)

        self.width = width
        self.height = height

        self.initUI()
        self.generateMatrix()

    def initUI(self):
        self.setWindowTitle("MatrixCalc")
        self.setFixedSize(750, 480)

    def generateMatrix(self):
        self.grid = QGridLayout()
        self.grid.setGeometry(QtCore.QRect(5, 5, 5, 5))
        
        #Генерация пустой матрицы
        for h in range(self.height):
            for w in range(self.width):
                btn = QtWidgets.QLineEdit(self)
                btn.setFixedWidth(35)
                self.grid.addWidget(btn, h, w, 10, 10)
        self.setLayout(self.grid)
                
            


# Экземпляр класса QApplication
app = QtWidgets.QApplication(sys.argv)
# Csоздание инстанса App
graphs = App()
# Запуск
sys.exit(app.exec_())