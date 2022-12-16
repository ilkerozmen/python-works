import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tableForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()

        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def loadProducts(self):
        
        products = [
            {'Name': 'Samsung S5', 'Price': 2000},
            {'Name': 'Samsung S6', 'Price': 3000},
            {'Name': 'Samsung S7', 'Price': 4000},
            {'Name': 'Samsung S8', 'Price': 5000}
        ]
        
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name','Price'))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex = 0
        for i in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(i['Name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(i['Price'])))
            rowIndex += 1

        # self.ui.tableProducts.setItem(0,0, QTableWidgetItem('Samsung S5'))
        # self.ui.tableProducts.setItem(0,1, QTableWidgetItem('2000'))
        # self.ui.tableProducts.setItem(1,0, QTableWidgetItem('Samsung S6'))
        # self.ui.tableProducts.setItem(1,1, QTableWidgetItem('3000'))
        # self.ui.tableProducts.setItem(2,0, QTableWidgetItem('Samsung S7'))
        # self.ui.tableProducts.setItem(2,1, QTableWidgetItem('4000'))

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtFiyat.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(str(price)))

    def doubleClick(self):    # çift tıklanan parselin satır kolon içeriğini verir.
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(), item.column(), item.text())
  

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()