import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from msgboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):
                                     # Alt satır ram li alanın kısa yolu.
        result = QMessageBox.question(self, 'Close Application','Are you sure?', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes Clicked')
            QtWidgets.qApp.quit()
        else:
            print('No Clicked')   


"""
        msg = QMessageBox()

        msg.setWindowTitle('Close Application')
        msg.setText('Are you sure?')
        msg.setIcon(QMessageBox.Warning)    # Warning iconu çıkar.
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Cancel)   # Cancel butonu seçili olarak gelir.
        msg.setDetailedText('details....')   # Show detail butonu ekler ve açıklama kısmına verilen string ifadeyi yazar.
        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()
        print(x)

    
    def popup_button(self,i):
        print(i.text()

        if i.text() == 'OK':
            print('OKEY')
            QtWidgets.qApp.quit()
        elif i.text() == 'Cancel':
            print('Cancel...')
        else:
            print('Ignore...')
"""


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()