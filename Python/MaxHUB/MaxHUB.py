__author__ = "Maxim"

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from model.model import Model
from view.view import Ui_MainWindow
from control.control import Control

if __name__ == '__main__':
    app = QApplication()
    model = Model()
    view = Ui_MainWindow()
    control = Control(model, view)
    control.show()
    sys.exit(app.exec())
