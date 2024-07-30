from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
import authentication
from heads_window import Ui_HeadsWindow
from local_board_window_1 import Ui_LocalBoard1Window

class Ui_LoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(800, 600))
        LoginWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(250, 60, 361, 141))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, -40, 821, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())
        self.background_label.setSizePolicy(sizePolicy)
        self.background_label.setObjectName("background_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 230, 301, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 490, 301, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 350, 301, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f91; /* Border color */\n"
"    border-radius: 15px;       /* Corner roundness */\n"
"    padding: 6px;              /* Padding inside the widget */\n"
"    background-color: #ffffff; /* Background color */\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-20, -40, 271, 271))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/EUROAVIA_Logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 50, 111, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/images-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.back_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(20, 490, 111, 51))
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
        self.background_label.raise_()
        self.login_label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.back_pushButton.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.login_label.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#ffffff;\">Login</span></p><p align=\"center\"><br/></p></body></html>"))
        self.background_label.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\":/newPrefix/EUROAVIA_Logo.png\"/></p></body></html>"))
        self.label.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">USERNAME:</span></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">PASSWORD:</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))
        self.back_pushButton.setText(_translate("LoginWindow", "MENU"))

        qpixmap = QPixmap("images/EUROAVIA_Logo.png")
        self.background_label.setPixmap(qpixmap)
        qpixmap = QPixmap("images/EUROAVIA_Logo.png")
        self.label_3.setPixmap(qpixmap)
        qpixmap = QPixmap("images/images-removebg-preview.png")
        self.label_4.setPixmap(qpixmap)

        self.pushButton.clicked.connect(self.login)



    def login(self):
        ui_heads_window = Ui_HeadsWindow()
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        credentials = authentication.write_and_read_credentials()
        users_list = []
        for item in credentials.values():
            for my_dict in item:
                users_list.append(my_dict['user'])
        if user not in users_list:
            QMessageBox.critical(self, "ERROR", "USER INEXISTENT!")
            self.lineEdit.clear()
            return False
        else:
            for item in credentials.keys():
                for my_dict in credentials[item]:
                    if user == my_dict['user']:
                        if password == my_dict['password']:
                            if item == 'heads':
                                self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(3))
                                return True
                            elif item == 'local_board':
                                self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(4))
                                return True
                        else:
                            QMessageBox.critical(self, "ERROR", "PAROLA INVALIDA!")
                            self.lineEdit_2.clear()
                            return False




