from PyQt5 import QtCore, QtGui, QtWidgets
import Baza
from PyQt5.QtWidgets import QMessageBox
from ranking import Ui_ranking
import sys
from StworzQuizWindow import Ui_Form
from QuizWindow import Ui_Pytanie
class Ui_QUIZING(object):

    def after_clik_button(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        #QUIZING.close()
        self.window.show()


    def after_clik_buttonZagraj(self):
        QUIZING.close()
        Zagraj.show()

    def after_clik_button3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ranking()
        self.ui.setupUi(self.window)
        # QUIZING.close()
        self.window.show()

    def setupUi(self, QUIZING):
        QUIZING.setObjectName("QUIZING")
        QUIZING.resize(393, 280)
        self.pushButton = QtWidgets.QPushButton(QUIZING)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 151, 71))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.after_clik_button)

        self.pushButtonZagraj = QtWidgets.QPushButton(QUIZING)
        self.pushButtonZagraj.setGeometry(QtCore.QRect(210, 50, 151, 71))
        self.pushButtonZagraj.setObjectName("pushButtonZagraj")


        self.pushButtonZagraj.clicked.connect(self.after_clik_buttonZagraj)

        self.pushButton_3 = QtWidgets.QPushButton(QUIZING)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 180, 211, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.after_clik_button3)

        self.retranslateUi(QUIZING)
        QtCore.QMetaObject.connectSlotsByName(QUIZING)

    def retranslateUi(self, QUIZING):
        _translate = QtCore.QCoreApplication.translate
        QUIZING.setWindowTitle(_translate("QUIZING", "Form"))
        self.pushButton.setText(_translate("QUIZING", "Stwórz QUIZ!"))
        self.pushButtonZagraj.setText(_translate("QUIZING", "Zagraj!"))
        self.pushButton_3.setText(_translate("QUIZING", "Ranking"))


class Ui_Zagraj(Ui_QUIZING):

    def after_clik_buttonWroc(self):
        QUIZING.show()
        Zagraj.close()


    def after_clik_buttonZagraj(self):

        itms = self.listView.selectedIndexes()
        if(itms.__sizeof__() == 40):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Brak kategorii")
            self.msg.setInformativeText("Wybierz kategorię!")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()

        if(self.lineEdit.text() == ""):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Brak imienia")
            self.msg.setInformativeText("Wpisz imie!")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()

        for it in itms:
            if(Baza.pobierzPytania(it.data()).__len__() < 10):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Mało pytań")
                self.msg.setInformativeText("Ta kategoria ma mniej niż 10 pytań.")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.show()
                pass
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Pytanie()
                self.ui.setupUi(self.window, it.data(), self.lineEdit.text())
                self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 471)
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
        self.pushButton.setGeometry(QtCore.QRect(400, 430, 111, 27))
        self.pushButton.setObjectName("pushButtonZagraj")
        self.pushButtonWroc = QtWidgets.QPushButton(Form)
        self.pushButtonWroc.setGeometry(QtCore.QRect(280, 430, 101, 27))
        self.pushButtonWroc.setObjectName("pushButtonWroc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 10, 261, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(390, 360, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 340, 91, 17))
        self.label_2.setObjectName("label_2")

        self.pushButtonWroc.clicked.connect(self.after_clik_buttonWroc)
        self.pushButton.clicked.connect(self.after_clik_buttonZagraj)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Zagraj"))
        self.pushButtonWroc.setText(_translate("Form", "Wroc"))
        self.label.setText(_translate("Form", "Wybierz kategorie i graj!"))
        self.label_2.setText(_translate("Form", "Twoje imie"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QUIZING = QtWidgets.QMainWindow()
    ui = Ui_QUIZING()
    ui.setupUi(QUIZING)

    Zagraj = QtWidgets.QMainWindow()
    uiZ = Ui_Zagraj()
    uiZ.setupUi(Zagraj)




    QUIZING.show()
    sys.exit(app.exec_())

