from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import Baza
class Ui_listaPytan(object):
    def setupUi(self, Form1, kategoria):
        Form1.setObjectName("Form")
        Form1.resize(300, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 300, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")



        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listView.setGeometry(0,0,300,600)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        lista = Baza.pobierzPytania(kategoria)
        if(lista.__len__() == 0):
            self.listView.addItem(''.join("Brak pytań. Dodaj je!"))
        for i in lista:
            self.listView.addItem(''.join(i))


        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QMainWindow()
        uiF = Ui_listaPytan()
        uiF.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())