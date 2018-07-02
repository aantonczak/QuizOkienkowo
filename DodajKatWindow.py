import Baza
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dodajKategorie(object):

    def after_clik_button(self):
        Baza.dodajKategorie(self.lineEdit.text())
        self.lineEdit.clear()


    def setupUi(self, dodajKategorie):
        dodajKategorie.setObjectName("dodajKategorie")
        dodajKategorie.resize(400, 234)
        self.lineEdit = QtWidgets.QLineEdit(dodajKategorie)
        self.lineEdit.setGeometry(QtCore.QRect(72, 50, 251, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(dodajKategorie)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 151, 27))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.after_clik_button)

        self.retranslateUi(dodajKategorie)
        QtCore.QMetaObject.connectSlotsByName(dodajKategorie)

    def retranslateUi(self, dodajKategorie):
        _translate = QtCore.QCoreApplication.translate
        dodajKategorie.setWindowTitle(_translate("dodajKategorie", "Form"))
        self.pushButton.setText(_translate("dodajKategorie", "Dodaj kategorie"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    dodajKategorieOkno = QtWidgets.QMainWindow()
    uiK = Ui_dodajKategorie()
    uiK.setupUi(dodajKategorieOkno)
    dodajKategorieOkno.show()


    sys.exit(app.exec_())