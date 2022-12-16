import sys
from PyQt5 import QtWidgets
from radiobuttonForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radiolise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)

        self.ui.radiolise.toggled.connect(self.onClickedegitim)
        self.ui.radiouniversite.toggled.connect(self.onClickedegitim)
        self.ui.radioilkokul.toggled.connect(self.onClickedegitim)
        self.ui.radioyukseklisans.toggled.connect(self.onClickedegitim)

        self.ui.btnulke.clicked.connect(self.getSelectedUlke)
        self.ui.btnegitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print('Seçilen radio: '+ rb.text())

    def onClickedegitim(self):
        rb = self.sender()
        if rb.isChecked():
            print('Seçilen radio: '+ rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText('Seçilen Ülke: '+ rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText('Seçilen Eğitim: '+ rb.text())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()