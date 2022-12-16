import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox
from listForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load Students
        self.loadStudents()

        # add new student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # edit student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # delete student
        self.ui.btnRemove.clicked.connect(self.deleteStudent)

        # UP
        self.ui.btnUp.clicked.connect(self.upStudent)

        # DOWN
        self.ui.btnDown.clicked.connect(self.downStudent)

        # SORT
        self.ui.btnSort.clicked.connect(self.sortStudent)

        # SORT
        self.ui.btnExit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet','Ali','Çınar'])
        self.ui.listItems.setCurrentRow(0)   # ilk eleman seçili olarak gelir.

    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        text, ok =  QInputDialog.getText(self, "New Student","Student Name")
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex, text)

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def deleteStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        
        if item is None:
            return

        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student ? : "+ item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >=1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count()-1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudent(self):
        self.ui.listItems.sortItems()
        
    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()