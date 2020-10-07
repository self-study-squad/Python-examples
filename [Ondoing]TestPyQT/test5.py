# Test new PyThon GUI

import sys
import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
try: 
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) <2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours),int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv)>2:
        message =" ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [Optional Message]"

while QTime.currentTime() < due:
    time.sleep(20)

label = QtWidgets.QLabel("<font color = red size = 72><b>" + message + "</b></font>")
label.setWindowsFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(6000,app.quit)
app.exec_()

