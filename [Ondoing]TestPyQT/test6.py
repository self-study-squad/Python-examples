# Test 06 about UI

import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PenPropDlg(QDialog):
    def __init__(self,parent=none):
        super(PenPropDlg,self)__init__(parent)

        widthLabel = Qlabel("&Width: ")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinBox.setRange(0,24)
        self.beveledCheckBox = QCheckBox("&Belved edges")
        styleLabel = Qlabel("&Style: ")
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid","Dashed","Dotted","DashDotted","DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel,0,0)
        layout.addWidget(self.widthSpinBox,0,1)
        layout.addWidget(self.belvedCheckBox,0,2)
        layout.addWidget(styleLabel,1,0)
        layout.addWidget(self.styleComboBox,1,1,1,2)
        layout.addLayout(buttonLayout,2,0,1,3)
        self.setLayout(layout)

def setPenProp(self):
    dialog = PenPropDlg(self)
    dialog.widthSpinBox.setValue(self.width)
    dialog.beveledCheckBox.setChecked(self.beveled)
    dialog.styleComboBox.setCurrentIndex(dialog.styleComboBox.findText(self.style))
    if dialog.exec_():
        self.width = dialog.widthSpinBox.value()
        self.beveled = dialog.beveledCheckBox.isChecked()
        self.style = unicode(dialog.styleComboBox.currentText())
        self.updateData()
        self.connect(okButton,SIGNAL("clicked()"),self,SLOT("accept()"))
        self.connect(cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.setWindowTitle("Pen Properties")

app = QApplication([])
setPenProp(app)
app.exec_()