# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qlhsPop.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1010, 628)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 991, 591))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.thsm = QtWidgets.QPushButton(self.layoutWidget)
        self.thsm.setObjectName("thsm")
        self.gridLayout.addWidget(self.thsm, 0, 0, 1, 1)
        self.qlshPop_table = QtWidgets.QTableView(self.layoutWidget)
        self.qlshPop_table.setObjectName("qlshPop_table")
        self.gridLayout.addWidget(self.qlshPop_table, 1, 0, 1, 2)
        self.xndd = QtWidgets.QPushButton(self.layoutWidget)
        self.xndd.setObjectName("xndd")
        self.gridLayout.addWidget(self.xndd, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.thsm.setText(_translate("Dialog", "Thêm học sinh mới"))
        self.xndd.setText(_translate("Dialog", "Xác nhận điểm danh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
