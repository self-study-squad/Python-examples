# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 90, 231, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qlhs = QtWidgets.QPushButton(self.layoutWidget)
        self.qlhs.setMinimumSize(QtCore.QSize(111, 28))
        self.qlhs.setObjectName("qlhs")
        self.verticalLayout.addWidget(self.qlhs)
        self.qlgv = QtWidgets.QPushButton(self.layoutWidget)
        self.qlgv.setMinimumSize(QtCore.QSize(93, 28))
        self.qlgv.setObjectName("qlgv")
        self.verticalLayout.addWidget(self.qlgv)
        self.qlhp = QtWidgets.QPushButton(self.layoutWidget)
        self.qlhp.setMinimumSize(QtCore.QSize(93, 28))
        self.qlhp.setObjectName("qlhp")
        self.verticalLayout.addWidget(self.qlhp)
        self.pmvn = QtWidgets.QPushButton(self.layoutWidget)
        self.pmvn.setMinimumSize(QtCore.QSize(93, 28))
        self.pmvn.setObjectName("pmvn")
        self.verticalLayout.addWidget(self.pmvn)
        self.ptln = QtWidgets.QPushButton(self.layoutWidget)
        self.ptln.setMinimumSize(QtCore.QSize(93, 28))
        self.ptln.setObjectName("ptln")
        self.verticalLayout.addWidget(self.ptln)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qlhs.setText(_translate("MainWindow", "Quản Lý Học Sinh"))
        self.qlgv.setText(_translate("MainWindow", "Quản Lý Giáo Viên"))
        self.qlhp.setText(_translate("MainWindow", "Quản Lý Học Phí"))
        self.pmvn.setText(_translate("MainWindow", "Phân môn và nhóm"))
        self.ptln.setText(_translate("MainWindow", "Phân tích lợi nhuận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
