# Test for PyQT

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("Hello Qt")
window.show()
app.exec()