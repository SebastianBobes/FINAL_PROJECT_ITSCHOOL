from PyQt6 import QtCore, QtGui, QtWidgets


from application_form import Ui_FormWindow
from menu import Ui_MenuWindow
from login import LoginWindow





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("images/rocket.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FormWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())





