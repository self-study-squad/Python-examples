from uicnvpy1 import *
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QComboBox
import mysql.connector
from PyQt5 import uic
from tkinter import messagebox

class CsdlKhanhVu:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', passwd='Mysql', database='kvdatabase')
            self.curs = self.conn.cursor()
        except mysql.connector.Error as err:
            #QMessageBox.setInformativeText(err)
            messagebox.showerror(err)
    def dongCsdlKhanhVu(self):
        self.curs.close()
        self.conn.close()
    def ghiThongTin(self, tenbang,tencot,noidung):
        tb = tenbang
        tc = tencot
        nd = noidung
        cmd = "INSERT INTO {} ({}) VALUES ({})".format(tb, tc, nd)
        try:
            self.curs.execute(cmd)
            self.conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror(err)
            self.curs.close()
            self.conn.close()
    def layThongTin(self):
        try:
            cmd = 'SELECT TenGV FROM dsgiaovien'
            self.curs.execute(cmd)
            kq = self.curs.fetchall()
            print(kq)
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layTenMonHoc(self):
        try:
            cmd = 'SELECT TenMonHoc FROM dmmonhoc'
            self.curs.execute(cmd)
            kq = self.curs.fetchall()
            listChuoiTenMonHoc = []
            for i in kq:
                cnvToStr = str(i)
                listChuoiTenMonHoc.append(cnvToStr[2:-3])
            return listChuoiTenMonHoc
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layMaGiaoVien(self):
        try:
            cmd = 'SELECT MaGV FROM dsgiaovien'
            self.curs.execute(cmd)
            kq = self.curs.fetchall()
            listMaGV = []
            for i in kq:
                listMaGV.append(str(i)[1:-2])
            return listMaGV
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layTenGiaoVienFromMaGiaoVien(self):
        try:
            mgv = w.ui.cbbMGVtwDSN.currentText()
            cmd = "SELECT TenGV FROM dsgiaovien WHERE MaGV = {}".format(mgv)
            self.curs.execute(cmd)
            kq = str(self.curs.fetchone())[2:-3]
            w.ui.lblTenGVtwDSN.setText(kq)
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layTenNhom(self):
        try:
            cmd = "SELECT TenNhom FROM dsnhom"
            self.curs.execute(cmd)
            kq = self.curs.fetchall()
            listDSMN = []
            for x in kq:
                listDSMN.append(str(x)[2:-3])
            return listDSMN
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layMaHocSinh(self):
        try:
            cmd = "SELECT MaHS FROM dshocsinh"
            self.curs.execute(cmd)
            kq = self.curs.fetchall()
            listMaHS = []
            for i in kq:
                listMaHS.append(str(i)[1:-2])
            return listMaHS
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layTenHSFromMaHStwHSTN(self):
        try:
            mahs = w.ui.cbbMHStwHSTN.currentText()
            cmd = "SELECT HoTenHS FROM dshocsinh WHERE MaHS = {}".format(mahs)
            self.curs.execute(cmd)
            tenHS = str(self.curs.fetchone())[2:-3]
            w.ui.lblTHStwHSTN.setText(tenHS)
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def layTenHSFromMaHStwTHP(self):
        try:
            mahs = w.ui.cbbMHStwTHP.currentText()
            cmd = "SELECT HoTenHS FROM dshocsinh WHERE MaHS = {}".format(mahs)
            self.curs.execute(cmd)
            tenHS = str(self.curs.fetchone())[2:-3]
            w.ui.lblTHStwTHP.setText(tenHS)
        except mysql.connector.Error as err:
            messagebox.showerror(err)

class MyUI(QDialog):
    def __init__(self):
        super().__init__()  #kế thừa init của lớp cha, có thể lớp cha là pyqt5
        self.callcsdl = CsdlKhanhVu()
        self.MainWin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWin)
        self.MainWin.show()
    def xntwThongTin(self):
        tenBang = 'dshocsinh'
        tenCot = 'MaHS, HoTenHS,NamSinh, SoDienThoai, NgayVaoHoc, Lop'
        noiDung = "'" + self.ui.leMHStwTTHS.text() + "','" + \
                        self.ui.leHTHStwTTHS.text() + "','" + \
                        self.ui.leNSHStwTTHS.text() + "','" + \
                        self.ui.leSDTHStwTTHS.text() + "','" + \
                        self.ui.leNVHtwTTHS.text() + "','" + \
                        self.ui.leLtwTTHS.text() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)
    def xntwGiaoVien(self):
        tenBang = 'dsgiaovien'
        tenCot = 'MaGV, TenGV'
        noiDung = "'" + self.ui.leMGVtwDSGV.text() + "','" + \
                        self.ui.leTGVtwDSGV.text() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)
    def xntwDanhMucMonHoc(self):
        tenBang = 'dmmonhoc'
        tenCot = 'MaMonHoc, TenMonHoc'
        noiDung = "'" + self.ui.leMMHtwDMMH.text() + "','" + \
                        self.ui.leTMHtwDMMH.text() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)
    def xntwDanhSachNhom(self):
        tenBang = 'dsnhom'
        tenCot = 'MaNhom, TenNhom, TenMonHoc, MaGV'
        noiDung = "'" + self.ui.leMNtwDSN.text() + "','" + \
                        self.ui.leTNtwDSN.text() + "','" + \
                        self.ui.cbbMMHtwDSN.currentText() + "','" + \
                        self.ui.cbbMGVtwDSN.currentText() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)
    def xntwHocSinhTheoNhom(self):
        tenBang = 'hstheonhom'
        tenCot = 'TenNhom, MaHS'
        noiDung = "'" + self.ui.cbbMNtwHSTN.currentText() + "','" + \
                        self.ui.cbbMHStwHSTN.currentText() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)
    def xntwThuHocPhi(self):
        tenBang = 'thuhocphi'
        tenCot = 'MaHS, NgayDongTien'
        noiDung = "'" + self.ui.cbbMHStwTHP.currentText() + "','" + \
                        self.ui.leNTtwTHP.text() + "'"
        self.callcsdl.ghiThongTin(tenbang=tenBang, tencot=tenCot, noidung=noiDung)

def showdata(self):
        csdl = CsdlKhanhVu()
        csdl.layTenMonHoc()


if __name__ == "__main__":
    app = QApplication(sys.argv)    #
    callCsdlMain = CsdlKhanhVu()
    w = MyUI()
    w.ui.btnshow.clicked.connect(showdata)
    w.ui.btnXNtwTTHS.clicked.connect(w.xntwThongTin)
    w.ui.btnXNtwDSGV.clicked.connect(w.xntwGiaoVien)
    w.ui.btnXNtwDMMH.clicked.connect(w.xntwDanhMucMonHoc)
    #w.ui.cbbTMHtwDSN.insertItems(0, callCsdlMain.layTenMonHoc())     # cbb ten mon hoc tw dsnhom
    w.ui.cbbMGVtwDSN.insertItems(0, callCsdlMain.layMaGiaoVien())    # cbb ma gv tw dsnhom
    mgvMain = w.ui.cbbMGVtwDSN.currentText()
    if mgvMain != "":
        callCsdlMain.layTenGiaoVienFromMaGiaoVien()
    w.ui.cbbMGVtwDSN.currentTextChanged.connect(callCsdlMain.layTenGiaoVienFromMaGiaoVien)
    w.ui.btnXNtwDSN.clicked.connect(w.xntwDanhSachNhom)
    #w.ui.cbbTNtwHSTN.insertItems(0, callCsdlMain.layTenNhom())
    w.ui.cbbMHStwHSTN.insertItems(0, callCsdlMain.layMaHocSinh())
    if w.ui.cbbMHStwHSTN.currentText() != "":
        callCsdlMain.layTenHSFromMaHStwHSTN()
    w.ui.cbbMHStwHSTN.currentTextChanged.connect(callCsdlMain.layTenHSFromMaHStwHSTN)
    w.ui.btnXNtwHSTN.clicked.connect(w.xntwHocSinhTheoNhom)
    #w.ui.cbbTNtwTHP.insertItems(0, callCsdlMain.layTenNhom())
    w.ui.cbbMHStwTHP.insertItems(0, callCsdlMain.layMaHocSinh())
    if w.ui.cbbMHStwTHP.currentText() != "":
        callCsdlMain.layTenHSFromMaHStwTHP()
    w.ui.cbbMHStwTHP.currentTextChanged.connect(callCsdlMain.layTenHSFromMaHStwTHP)
    sys.exit(app.exec_())




