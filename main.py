import sys
from PyQt6 import QtWidgets, QtGui, QtCore

import authentication
from menu import Ui_MenuWindow
from application_form import Ui_FormWindow
from login import Ui_LoginWindow
from heads_window import Ui_HeadsWindow
from local_board_window_1 import Ui_LocalBoard1Window
from local_board_window_2 import Ui_LocalBoard2Window
from change_pass import Ui_ChangePassWindow

def start_login_window():
    widget.setCurrentWidget(ui_login_window)

def start_form_window():
    widget.setCurrentWidget(ui_form_window)

def start_menu_window():
    widget.setCurrentWidget(ui_menu_window)

def show_heads_window():
    widget.setCurrentWidget(ui_heads_window)

def show_local_board1_window():
    widget.setCurrentWidget(ui_local_board_window_1)

def show_local_board2_window():
    widget.setCurrentWidget(ui_local_board_window_2)
def show_change_pass_window():
    widget.setCurrentWidget(ui_change_pass)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    app.setWindowIcon(QtGui.QIcon("images/rocket.png"))
    widget.setMaximumSize(800, 600)
    widget.setMinimumSize(800, 600)

    ui_change_pass  = Ui_ChangePassWindow()
    ui_change_pass.setupUi(ui_change_pass)
    widget.addWidget(ui_change_pass)

    ui_login_window = Ui_LoginWindow(widget)
    ui_login_window.setupUi(ui_login_window)
    widget.addWidget(ui_login_window)
    ui_login_window.back_pushButton.clicked.connect(start_menu_window)


    ui_menu_window = Ui_MenuWindow()
    ui_menu_window.setupUi(ui_menu_window)
    widget.addWidget(ui_menu_window)

    ui_form_window = Ui_FormWindow()
    ui_form_window.setupUi(ui_form_window)
    widget.addWidget(ui_form_window)


    ui_heads_window = Ui_HeadsWindow()
    ui_heads_window.setupUi(ui_heads_window)
    widget.addWidget(ui_heads_window)



    ui_local_board_window_1 = Ui_LocalBoard1Window()
    ui_local_board_window_1.setupUi(ui_local_board_window_1)
    widget.addWidget(ui_local_board_window_1)



    ui_local_board_window_2 = Ui_LocalBoard2Window()
    ui_local_board_window_2.setupUi(ui_local_board_window_2)
    widget.addWidget(ui_local_board_window_2)

    ui_form_window.back_pushButton.clicked.connect(start_menu_window)
    ui_menu_window.pushButton_2.clicked.connect(start_login_window)
    ui_menu_window.pushButton.clicked.connect(start_form_window)
    ui_local_board_window_1.next_page_pushButton.clicked.connect(show_local_board2_window)
    ui_local_board_window_2.previous_page_button.clicked.connect(show_local_board1_window)
    ui_heads_window.change_password_button.clicked.connect(show_change_pass_window)
    ui_local_board_window_1.change_password_button.clicked.connect(show_change_pass_window)
    ui_local_board_window_1.back_pushButton.clicked.connect(start_menu_window)

    ui_change_pass.back_pushButton.clicked.connect(start_menu_window)
    ui_heads_window.back_pushButton.clicked.connect(start_menu_window)
    widget.setCurrentWidget(ui_menu_window)
    widget.show()

    sys.exit(app.exec())












