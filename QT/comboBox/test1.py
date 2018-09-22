import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QGridLayout
from PyQt5.QtWidgets import QPushButton, QTextEdit, QComboBox, QMessageBox, QMainWindow
from PyQt5.QtCore import pyqtSignal

class MyComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()

    def __init__(self):
        super().__init__()

    def showPopup(self):
        print(self.currentText())
        QComboBox.showPopup(self) #弹出选项框

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        test1 = MyComboBox()
        self.makeItem(test1)
        grid.addWidget(test1, 0, 0)

        self.setLayout(grid)
        self.setWindowTitle('database backup')
        self.show()

    def makeItem(self, cb):
        for i in range(1, 11):
            cb.insertItem(i-1, str(i))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
