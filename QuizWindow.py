from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import Baza
class Ui_Pytanie(object):

    licznik = 1
    wynik = 0

    def after_clik_buttonNastepny(self,listaPytan, imie, kategoria):

        if(self.radioButton.isChecked() and listaPytan[self.licznik-1][1] == listaPytan[self.licznik-1][6]):
            self.wynik = self.wynik+1
            self.radioButton.setChecked(False)
        elif (self.radioButton_2.isChecked() and listaPytan[self.licznik - 1][2] == listaPytan[self.licznik - 1][6]):
            self.wynik = self.wynik + 1
            self.radioButton_2.setChecked(False)
        elif (self.radioButton_3.isChecked() and listaPytan[self.licznik - 1][3] == listaPytan[self.licznik - 1][6]):
            self.wynik = self.wynik + 1
            self.radioButton_3.setChecked(False)
        elif (self.radioButton_4.isChecked() and listaPytan[self.licznik - 1][4] == listaPytan[self.licznik - 1][6]):
            self.wynik = self.wynik + 1
            self.radioButton_4.setChecked(False)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", listaPytan[self.licznik][1]))
        self.label_2.setText(_translate("Form", listaPytan[self.licznik][2]))
        self.label_3.setText(_translate("Form", listaPytan[self.licznik][3]))
        self.label_4.setText(_translate("Form", listaPytan[self.licznik][4]))
        self.label_5.setText(_translate("Form", listaPytan[self.licznik][5]))
        self.licznik = self.licznik+1




        if(self.licznik == listaPytan.__len__() or self.licznik == 10):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Koniec")
            self.msg.setInformativeText("Wynik: "+ str(self.wynik))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
            self.label.setText(_translate("Form", ""))
            self.label_2.setText(_translate("Form", ""))
            self.label_3.setText(_translate("Form", ""))
            self.label_4.setText(_translate("Form", ""))
            self.label_5.setText(_translate("Form", ""))
            self.radioButton_4.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton.setChecked(False)

            Baza.dodajOsobe(imie,self.wynik,kategoria)
            self.pushButton.hide()




    def setupUi(self, Form, kategoria, imie):
        Form.setObjectName("Form")
        Form.resize(416, 366)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 320, 98, 27))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(-120, 40, 591, 281))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(130, 30, 116, 22))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 220, 116, 22))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 90, 116, 22))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(130, 150, 116, 22))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 66, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 66, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 66, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 260, 66, 17))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form,kategoria, imie)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form,kategoria, imie):

        listaPytan = Baza.pobierzWszystkoZKategorii(kategoria)


        self.pushButton.clicked.connect(lambda: self.after_clik_buttonNastepny(listaPytan, imie, kategoria))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", listaPytan[0][1]))
        self.pushButton.setText(_translate("Form", "Nastepne"))
        self.label_2.setText(_translate("Form", listaPytan[0][2]))
        self.label_3.setText(_translate("Form", listaPytan[0][3]))
        self.label_4.setText(_translate("Form", listaPytan[0][4]))
        self.label_5.setText(_translate("Form", listaPytan[0][5]))

        #while licznik < 3:


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Pytanie()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())