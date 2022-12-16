import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon('hat.png'))
    win.setToolTip('My Tooltip')

    win.show()
    sys.exit(app.exec_())

window()