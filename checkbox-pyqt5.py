import sys
from PyQt5 import QtWidgets
from checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cb_KitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.cbMatematik.stateChanged.connect(self.show_state)
        self.ui.cb_Programlama.stateChanged.connect(self.show_state)
        self.ui.cbWebtasarim.stateChanged.connect(self.show_state)

        self.ui.btnDerslerSecilenleriAl.clicked.connect(self.getAllDersler)
        self.ui.btnHobiSecilenleriAl.clicked.connect(self.getAllHobiler)

    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        
        self.ui.lblResultHobiler.setText(result)

    def getAllDersler(self):
        result = ''
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        
        self.ui.lblResultDersler.setText(result)


    def show_state(self, value):
        cb = self.sender()
        # print(cb.text())
        # print(cb.isChecked())
        # print(value)
        
        # print(value)   # seçili ise 2 döner. Seçili değilse 0 döner.
        # print(self.ui.cbSinema.isChecked())  # Seçildi mi özelliği
        # print(self.ui.cbSinema.text())   # checkbox ın text ini verir.

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()