from PyQt6 import QtCore, QtGui, QtWidgets


from application_form import Ui_FormWindow
from menu import Ui_MenuWindow
from login import Ui_LoginWindow
import sys

def start_login_window():
    widget.setCurrentWidget(ui_login_window)
def start_form_window():
    widget.setCurrentWidget(ui_form_window)

def start_menu_window():
    widget.setCurrentWidget(ui_menu_window)






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

    widget.setCurrentWidget(ui_menu_window)
    widget.show()




    sys.exit(app.exec())





