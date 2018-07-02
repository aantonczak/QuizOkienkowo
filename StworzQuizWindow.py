from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import Baza
from StworzNowePytanie import Ui_Stworz
from DodajKatWindow import Ui_dodajKategorie
from ListaPytanWindow import Ui_listaPytan

class Ui_Form():

    def after_clik_buttonDodajPytanie(self):
        itms = self.listView.selectedIndexes()
        for it in itms:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Stworz()
            self.ui.setupUi(self.window, it.data())
            self.window.show()

    def after_clik_buttonDodajKat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_dodajKategorie()
        self.ui.setupUi(self.window)
        self.window.show()
        pass
        #dodajKategorieOkno.show()


    def after_clilk_buttonUsunKat(self):

        itms = self.listView.selectedIndexes()
        for it in itms:
           # self.refresh(it)
            Baza.usunKategorie(it.data())
            #self.listView.deleteLater(it.data())
            #self.listView.removeItemWidget(it)

        for SelectedItem in self.listView.selectedItems():
            self.listView.takeItem(self.listView.row(SelectedItem))

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Usuwanie kategorii")
        self.msg.setInformativeText("Usunięto!")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()


    def after_clik_buttonWyswietlPytania(self):
        itms = self.listView.selectedIndexes()
        for it in itms:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_listaPytan()
            self.ui.setupUi(self.window, it.data())
            self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 466)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        lista1 = Baza.pobierzKategorie()

        for i in lista1:
            if(str(i) != "('sqlite_sequence',)"):
                self.listView.addItem(''.join(i))




        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 120, 231, 27))
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.after_clik_buttonWyswietlPytania)

        self.pushButtonDodajPytanie = QtWidgets.QPushButton(Form)
        self.pushButtonDodajPytanie.setGeometry(QtCore.QRect(380, 180, 201, 27))
        self.pushButtonDodajPytanie.setObjectName("pushButtonDodajPytanie")

        self.pushButtonDodajPytanie.clicked.connect(self.after_clik_buttonDodajPytanie)

        self.pushButtonDodajKat = QtWidgets.QPushButton(Form)
        self.pushButtonDodajKat.setGeometry(QtCore.QRect(380, 270, 201, 27))
        self.pushButtonDodajKat.setObjectName("pushButtonDodajKat")

        self.pushButtonDodajKat.clicked.connect(self.after_clik_buttonDodajKat)

        self.pushButtonUsunKat = QtWidgets.QPushButton(Form)
        self.pushButtonUsunKat.setGeometry(QtCore.QRect(390, 320, 180, 27))
        self.pushButtonUsunKat.setObjectName("pushButtonUsunKat")

        self.pushButtonUsunKat.clicked.connect(self.after_clilk_buttonUsunKat)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Wyswietl pytania"))
        self.pushButtonDodajPytanie.setText(_translate("Form", "Dodaj pytanie"))
        self.pushButtonDodajKat.setText(_translate("Form", "Dodaj kategorie"))
        self.pushButtonUsunKat.setText(_translate("Form", "Usun kategorie"))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    uiF = Ui_Form()
    uiF.setupUi(Form)



    Form.show()
    sys.exit(app.exec_())
