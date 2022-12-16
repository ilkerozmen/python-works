import sys
from PyQt5 import QtWidgets
from comboboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbSehirler
        # combo.addItem('Ankara')
        # combo.addItem('Bursa')
        # combo.addItem('Tokat')
        # combo.addItem('İstanbul')
        # combo.addItems(['İzmir','Adana','Şanlıurfa'])
        
        self.ui.btnLoadItem.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClearItem.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

    def LoadItems(self):
        sehirler = ['İzmir','Adana','Şanlıurfa']
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        print(self.ui.cbSehirler.count())

        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))   # verilen index numarasına ait box ın text bilgisini yazar.

    def selectedChangedIndex(self, index):
        print(index)

    def selectedChangedText(self, text):
        print(text)

    def ClearItems(self):
        self.ui.cbSehirler.clear()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()