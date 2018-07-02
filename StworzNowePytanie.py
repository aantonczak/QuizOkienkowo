from PyQt5 import QtCore, QtGui, QtWidgets
import Baza
class Ui_Stworz(object):




    def after_clik_button2(self, kategoria):

        if(self.checkBox.isChecked()):
            Baza.dodajPytanie(kategoria, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                              self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_2.text())
            self.checkBox.setChecked(False)
        elif(self.checkBox_2.isChecked()):
            Baza.dodajPytanie(kategoria, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                              self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_3.text())
            self.checkBox_2.setChecked(False)
        elif (self.checkBox_3.isChecked()):
            Baza.dodajPytanie(kategoria, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                              self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_4.text())
            self.checkBox_3.setChecked(False)
        elif (self.checkBox_4.isChecked()):
            Baza.dodajPytanie(kategoria, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                              self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_5.text())
            self.checkBox_4.setChecked(False)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()


    def setupUi(self, Stworz, kategoria):
        Stworz.setObjectName("Stworz")
        Stworz.resize(585, 478)
        self.label = QtWidgets.QLabel(Stworz)
        self.label.setGeometry(QtCore.QRect(10, 40, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Stworz)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Stworz)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Stworz)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 101, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Stworz)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 101, 17))
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(Stworz)
        self.checkBox.setGeometry(QtCore.QRect(460, 100, 97, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Stworz)
        self.checkBox_2.setGeometry(QtCore.QRect(460, 170, 97, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Stworz)
        self.checkBox_3.setGeometry(QtCore.QRect(460, 240, 97, 22))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Stworz)
        self.checkBox_4.setGeometry(QtCore.QRect(460, 310, 97, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(Stworz)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 391, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Stworz)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 331, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Stworz)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 170, 331, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Stworz)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 240, 331, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Stworz)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 310, 331, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Stworz)
        self.pushButton.setGeometry(QtCore.QRect(170, 370, 171, 71))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.after_clik_button2(kategoria))

        self.retranslateUi(Stworz)
        QtCore.QMetaObject.connectSlotsByName(Stworz)

    def retranslateUi(self, Stworz):
        _translate = QtCore.QCoreApplication.translate
        Stworz.setWindowTitle(_translate("Stworz", "Form"))
        self.label.setText(_translate("Stworz", "Pytanie:"))
        self.label_2.setText(_translate("Stworz", "Odpowiedz A:"))
        self.label_3.setText(_translate("Stworz", "Odpowiedz B:"))
        self.label_4.setText(_translate("Stworz", "Odpowiedz C:"))
        self.label_5.setText(_translate("Stworz", "Odpowiedz D:"))
        self.checkBox.setText(_translate("Stworz", "Poprawna"))
        self.checkBox_2.setText(_translate("Stworz", "Poprawna"))
        self.checkBox_3.setText(_translate("Stworz", "Poprawna"))
        self.checkBox_4.setText(_translate("Stworz", "Poprawna"))
        self.pushButton.setText(_translate("Stworz", "DODAJ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stworz = QtWidgets.QMainWindow()
    ui = Ui_Stworz()
    ui.setupUi(Stworz)
    Stworz.show()
    sys.exit(app.exec_())
