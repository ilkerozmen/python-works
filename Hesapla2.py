from PyQt5 import QtWidgets
import sys
from Hesapla import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.toplama)
        self.ui.btn_cikarma.clicked.connect(self.cikarma)
        self.ui.btn_carpma.clicked.connect(self.carpma)
        self.ui.btn_bolme.clicked.connect(self.bolme)

    def toplama(self):
        result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))

    def cikarma(self):
        result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))

    def carpma(self):
        result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))

    def bolme(self):
        result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())
        self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))


def Application():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

Application()