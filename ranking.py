from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Baza
class Ui_ranking(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 359)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(170, 10, 66, 17))
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 40, 371, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        lista = Baza.pobierzRanking()
        print(lista[0][0])
        self.label_6.setText(_translate("Form", "RANKING"))
        self.label_3.setText(_translate("Form", "1. " + str(lista[0][1])+", wynik: " + str(lista[0][2])))
        self.label_9.setText(_translate("Form", "2. " + str(lista[1][1])+", wynik: " + str(lista[1][2])))
        self.label_10.setText(_translate("Form", "3. " + str(lista[2][1])+", wynik: " + str(lista[2][2])))
        self.label_7.setText(_translate("Form", "4. " + str(lista[3][1])+", wynik: " + str(lista[3][2])))
        self.label_11.setText(_translate("Form", "5. " + str(lista[4][1])+", wynik: " + str(lista[4][2])))
        self.label_8.setText(_translate("Form", "6. " + str(lista[5][1])+", wynik: " + str(lista[5][2])))
        if(lista.__len__() > 6):
            self.label_5.setText(_translate("Form", "7. " + str(lista[6][1])+", wynik: " + str(lista[6][2])))
        else:
            self.label_5.setText(_translate("Form", "7. "))

        if (lista.__len__() > 7):
            self.label_4.setText(_translate("Form", "8. " + str(lista[7][1])+", wynik: " + str(lista[7][2])))
        else:
            self.label_4.setText(_translate("Form", "8. "))

        if (lista.__len__() > 8):
            self.label_2.setText(_translate("Form", "9. "  + str(lista[8][1])+", wynik: " + str(lista[8][2])))
        else:
            self.label_2.setText(_translate("Form", "9. "))

        if (lista.__len__() > 9):
            self.label.setText(_translate("Form", "10. " + str(lista[9][1])+", wynik: " + str(lista[9][2])))
        else:
            self.label.setText(_translate("Form", "10. " ))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    uiF = Ui_ranking()
    uiF.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())