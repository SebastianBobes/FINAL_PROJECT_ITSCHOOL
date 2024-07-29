from tkinter import messagebox

from PyQt6 import QtCore, QtGui, QtWidgets

import authentication
from application_form import Ui_FormWindow
from menu import Ui_MenuWindow
from login import Ui_LoginWindow
from heads_window import Ui_HeadsWindow
import sys

def start_login_window():
    widget.setCurrentWidget(ui_login_window)
def start_form_window():
    widget.setCurrentWidget(ui_form_window)

def start_menu_window():
    widget.setCurrentWidget(ui_menu_window)

def show_heads_window():
    widget.setCurrentWidget(ui_heads_window)



def login():
    user = ui_login_window.lineEdit.text()
    password = ui_login_window.lineEdit_2.text()
    credentials = authentication.write_and_read_credentials()
    users_list = []
    for item in credentials.values():
        for my_dict in item:
            users_list.append(my_dict['user'])
    if user not in users_list:
        messagebox.showerror("ERROR", "USER INEXISTENT!")
        ui_login_window.lineEdit.clear()
        return False
    else:
        for item in credentials.values():
            for my_dict in item:
                if user == my_dict['user']:
                    if password == my_dict['password']:
                        show_heads_window()
                    else:
                        messagebox.showerror("ERROR", "PAROLA INVALIDA!")
                        ui_login_window.lineEdit_2.clear()
                        return False












if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    app.setWindowIcon(QtGui.QIcon("images/rocket.png"))
    widget.setMaximumSize(800,600)
    widget.setMinimumSize(800,600)

    ui_menu_window = Ui_MenuWindow()
    ui_menu_window.setupUi(ui_menu_window)
    widget.addWidget(ui_menu_window)
    ui_menu_window.pushButton_2.clicked.connect(start_login_window)
    ui_menu_window.pushButton.clicked.connect(start_form_window)


    ui_form_window = Ui_FormWindow()
    ui_form_window.setupUi(ui_form_window)
    widget.addWidget(ui_form_window)
    ui_form_window.back_pushButton.clicked.connect(start_menu_window)

    ui_login_window = Ui_LoginWindow()
    ui_login_window.setupUi(ui_login_window)
    widget.addWidget(ui_login_window)
    ui_login_window.back_pushButton.clicked.connect(start_menu_window)
    ui_login_window.pushButton.clicked.connect(login)

    ui_heads_window = Ui_HeadsWindow()
    ui_heads_window.setupUi(ui_heads_window)
    widget.addWidget(ui_heads_window)

    widget.setCurrentWidget(ui_menu_window)
    widget.show()







    sys.exit(app.exec())





