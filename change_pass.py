# Form implementation generated from reading ui file '.\change_pass.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit

import authentication


class Ui_ChangePassWindow(QMainWindow):
    def setupUi(self, ChangePassWindow):
        ChangePassWindow.setObjectName("ChangePassWindow")
        ChangePassWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangePassWindow.sizePolicy().hasHeightForWidth())
        ChangePassWindow.setSizePolicy(sizePolicy)
        ChangePassWindow.setMinimumSize(QtCore.QSize(800, 600))
        ChangePassWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=ChangePassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, -40, 821, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())
        self.background_label.setSizePolicy(sizePolicy)
        self.background_label.setObjectName("background_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.username_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(280, 150, 301, 41))
        self.username_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.change_pass_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.change_pass_pushButton.setGeometry(QtCore.QRect(290, 520, 301, 51))
        self.change_pass_pushButton.setStyleSheet("QPushButton {\n"
"    font-size: 14pt; /* Increase the font size as desired */\n"
"    font-family: \'Bahnschrift\'; /* Optional: Set the font family to Bahnschrift */\n"
"    font-weight: bold; /* Optional: Make the text bold */\n"
"    color: black; /* Set text color */\n"
"    background-color: white; /* Light gray background */\n"
"    border: none; /* Remove default border */\n"
"    padding: 10px; /* Add some padding */\n"
"    border-radius: 5px; /* Round the corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A9A9A9; /* Darker gray on hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #808080; /* Even darker gray on press */\n"
"}")
        self.change_pass_pushButton.setObjectName("change_pass_pushButton")
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(280, 240, 301, 41))
        self.password_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.logo_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(-20, -40, 221, 221))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/newPrefix/EUROAVIA_Logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.icon_labe = QtWidgets.QLabel(parent=self.centralwidget)
        self.icon_labe.setGeometry(QtCore.QRect(690, 10, 101, 131))
        self.icon_labe.setText("")
        self.icon_labe.setPixmap(QtGui.QPixmap(":/newPrefix/images-removebg-preview.png"))
        self.icon_labe.setScaledContents(True)
        self.icon_labe.setObjectName("icon_labe")
        self.back_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(20, 520, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Valoarea aceasta o poți ajusta pentru a obține rotunjimea dorită */\n"
"    border: 2px solid #ADD8E6; /* Bordura butonului */\n"
"    background-color:#ADD8E6; /* Culoarea de fundal a butonului */\n"
"    color: white; /* Culoarea textului */\n"
"    padding: 5px; /* Spațierea internă */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #87CEEB; /* Culoarea de fundal când mouse-ul este deasupra butonului */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5FA9D0; /* Culoarea de fundal când butonul este apăsat */\n"
"    border: 2px solid #5FA9D0; /* Bordura butonului când este apăsat */\n"
"}")
        self.back_pushButton.setObjectName("back_pushButton")
        self.new_password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.new_password_lineEdit.setGeometry(QtCore.QRect(280, 340, 301, 41))
        self.new_password_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.new_password_lineEdit.setObjectName("new_password_lineEdit")
        self.nre_password_2_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nre_password_2_lineEdit.setGeometry(QtCore.QRect(280, 420, 301, 41))
        self.nre_password_2_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.nre_password_2_lineEdit.setObjectName("nre_password_2_lineEdit")

        self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.nre_password_2_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 300, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.background_label.raise_()
        self.label_2.raise_()
        self.username_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.logo_label.raise_()
        self.change_pass_pushButton.raise_()
        self.icon_labe.raise_()
        self.label.raise_()
        self.back_pushButton.raise_()
        self.new_password_lineEdit.raise_()
        self.nre_password_2_lineEdit.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        ChangePassWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChangePassWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangePassWindow)

    def retranslateUi(self, ChangePassWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangePassWindow.setWindowTitle(_translate("ChangePassWindow", "MainWindow"))
        self.background_label.setText(_translate("ChangePassWindow", "<html><head/><body><p><img src=\":/newPrefix/EUROAVIA_Logo.png\"/></p></body></html>"))
        self.label.setText(_translate("ChangePassWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">USERNAME:</span></p></body></html>"))
        self.label_2.setText(_translate("ChangePassWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">PASSWORD:</span></p><p><br/></p></body></html>"))
        self.change_pass_pushButton.setText(_translate("ChangePassWindow", "CHANGE PASSWORD"))
        self.back_pushButton.setText(_translate("ChangePassWindow", "MENU"))
        self.label_5.setText(_translate("ChangePassWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">NEW PASSWORD:</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("ChangePassWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">NEW PASSWORD:</span></p><p><br/></p></body></html>"))
        self.label_7.setText(_translate("ChangePassWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#c8c8c8;\">CHANGE PASSWORD </span></p></body></html>"))
        qpixmap = QPixmap("images/EUROAVIA_Logo.png")
        self.background_label.setPixmap(qpixmap)
        qpixmap = QPixmap("images/EUROAVIA_Logo.png")
        self.logo_label.setPixmap(qpixmap)
        qpixmap = QPixmap("images/images-removebg-preview.png")
        self.icon_labe.setPixmap(qpixmap)

        self.change_pass_pushButton.clicked.connect(self.change_pass)

    def change_pass(self):
        """
        method created to change the pass from auth file
        :return:
        """
        user = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        new_password_1 = self.new_password_lineEdit.text()
        new_password_2 = self.nre_password_2_lineEdit.text()
        credentials = authentication.write_and_read_credentials()
        users_list = []
        for item in credentials.values():
            for my_dict in item:
                users_list.append(my_dict['user'])
        if user not in users_list:
            QMessageBox.critical(self, "ERROR", "USER INEXISTENT!")
            self.username_lineEdit.clear()
            return False
        else:
            for item in credentials.keys():
                for my_dict in credentials[item]:
                    if user == my_dict['user']:
                        if password == my_dict['password']:
                            if new_password_2 != new_password_1:
                                QMessageBox.critical(self, "ERROR", "PAROLELE NU SE POTRIVESC!")
                                self.nre_password_2_lineEdit.clear()
                                self.new_password_lineEdit.clear()
                            else:
                                if len(new_password_1) < 5:
                                    QMessageBox.critical(self, "ERROR", "PAROLA PREA SCURTA!")
                                    self.nre_password_2_lineEdit.clear()
                                    self.new_password_lineEdit.clear()
                                elif new_password_1.isdigit() == True:
                                    QMessageBox.critical(self, "ERROR", "PAROLA NU POATE CONTINE DOAR NUMERE!")
                                    self.nre_password_2_lineEdit.clear()
                                    self.new_password_lineEdit.clear()
                                elif new_password_1.isalpha() == True:
                                    QMessageBox.critical(self, "ERROR", "PAROLA NU POATE CONTINE DOAR LITERE")
                                    self.nre_password_2_lineEdit.clear()
                                    self.new_password_lineEdit.clear()
                                else:
                                    authentication.change_pass(user,new_password_1)
                                    QMessageBox.information(self, "Info", f"Parola a fost schimbata!")
                                    self.nre_password_2_lineEdit.clear()
                                    self.new_password_lineEdit.clear()
                                    self.username_lineEdit.clear()
                                    self.password_lineEdit.clear()


                        else:
                            QMessageBox.critical(self, "ERROR", "PAROLA INCORECTA!")
                            self.password_lineEdit.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePassWindow = QtWidgets.QMainWindow()
    ui = Ui_ChangePassWindow()
    ui.setupUi(ChangePassWindow)
    ChangePassWindow.show()
    sys.exit(app.exec())
