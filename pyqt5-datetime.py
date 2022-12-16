import sys
from PyQt5 import QtWidgets
from dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime         # https://zetcode.com/gui/pyqt5/datetime/

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.Calculate)

    
    def Calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        # print(start, end)

        # print('Days in month: {0}' .format(start.daysInMonth()))  # Ay içerisindeki gün sayısı
        # print('Days in year: {0}' .format(start.daysInYear()))   # Yıl içerisindeki gün sayısını verir.
        # print('Total Days: {0}'.format(start.daysTo(end)))   # iki tarih arasındaki gün sayısını verir.

        now = QDate.currentDate()

        print('Total Days: {0}'.format(start.daysTo(now)))   # şimdiki tarih ile geçmişte belirtilen tarih arasındaki gün sayısını verir.


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()