#GUI new test Subjects

import sys
import mysql.connector

from PyQt5 import uic

from TestUIDesign import *


class MyForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FindReplace()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())

