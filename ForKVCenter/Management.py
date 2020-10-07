import tkinter as tk
from tkinter import ttk
import mysql.connector
import datetime
from tkinter import messagebox


class MySQL:

    '''Cac tinh nang cua sql nhu xoa, chen, tao bang, ...'''

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', passwd='Mysql', database='databasemystudent')
            self.mycursor = self.conn.cursor()

        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def TaoBang(self, tenBang):
        sql = 'CREATE TABLE IF NOT EXISTS {}'.format(tenBang)
        self.mycursor.execute(sql)
    def ThemDuLieu(self, tenBangCanTruyen, noiDungCanTruyenTuEntry, tenCotTrongBangSTUDENT):       # insert tu 1 textb toi 1 cot trong bang
        tenCot = tenCotTrongBangSTUDENT
        noiDung = noiDungCanTruyenTuEntry
        tenBang = tenBangCanTruyen
        sql = "INSERT INTO {} ({}) VALUES ({})".format(tenBang, tenCot, noiDung)
        try:
            self.mycursor.execute(sql)
            self.conn.commit()
        except mysql.connector.Error as error:
            print('Failed to insert record {}'.format(error))
            messagebox.showerror(error)
    def LayToanBoDuLieuTuBang(self, bangNao):
        self.mycursor.execute('SELECT * FROM {}'.format(bangNao))
        mySelect = self.mycursor.fetchall()
        return mySelect
    def LayTenGiaoVien(self):
        lenhThucThi = 'SELECT TenGV FROM dsgiaovien'
        self.mycursor.execute(lenhThucThi)
        layToanBoTenGiaoVien = self.mycursor.fetchall() #nhan duoc 1 list nhung co '(' va ','; vd:[('Phạm Như Long',), ('Ngô Nguyễn Khánh An',)]
        #tao 1 list ten giao vien, chuoi thi se chay sai
        listChuoiTenGiaoVien = []
        for i in layToanBoTenGiaoVien:
            convert2str = str(i)
            listChuoiTenGiaoVien.append(convert2str[2:-3])
        return listChuoiTenGiaoVien
    def LayMaGiaoVien(self, tenGiaoVien):
        lenhThucThi = "SELECT MaGV FROM dsgiaovien WHERE TenGV='Phạm Như Long'".format(tenGiaoVien)
        maGiaoVien = self.mycursor.execute(lenhThucThi)
        print(maGiaoVien)
        return maGiaoVien


mainWindow = tk.Tk()
mainWindow.title('Quản lý')
mainWindow.geometry('800x550')

#khoi tao TAB dieu khien
tabControl = ttk.Notebook(mainWindow)
tabControl.pack(expand=1, fill='both')
chonRadioButtonMacDinh = tk.IntVar()    #tabDiemDanh
chonRadioButtonMacDinh.set(1)           #tabDiemDanh,su lua chon radio ban dau

def tabThongTin():
    def xacNhanTabThongTin():
        print('Chua Xac Nhan')
    frameThongTinHocSinh = tk.Frame(tabControl)
    tabControl.add(frameThongTinHocSinh, text='Thông tin học sinh')
    #students info
    chieuRongTextBoxTabThongTin = 25
    cotATabThongTin = 0
    cotBTabThongTin = cotATabThongTin + 100
    cotCTabThongTin = cotBTabThongTin + chieuRongTextBoxTabThongTin*7
    cotDTabThongTin = cotCTabThongTin + 120
    khoangCachGiua2DongTabThongTin = 35
    dongHienTaiTabThongTin = 20
    #ma hoc sinh
    lblMaHocsinh = tk.Label(frameThongTinHocSinh, text='Mã học sinh:')
    lblMaHocsinh.place(y=dongHienTaiTabThongTin, x=cotATabThongTin)
    tbMaHocSinhText = tk.StringVar()
    tbMaHocSinh = tk.Entry(frameThongTinHocSinh, textvariable=tbMaHocSinhText, width=chieuRongTextBoxTabThongTin)
    tbMaHocSinh.place(y=dongHienTaiTabThongTin, x=cotBTabThongTin)
    dongHienTaiTabThongTin += khoangCachGiua2DongTabThongTin
    #ten hoc sinh
    lblTenHocSinh = tk.Label(frameThongTinHocSinh, text='Tên học sinh:')
    lblTenHocSinh.place(y=dongHienTaiTabThongTin, x=cotATabThongTin)
    tbTenHocSinhText = tk.StringVar()
    tbTenHocSinh = tk.Entry(frameThongTinHocSinh, textvariable=tbTenHocSinhText, width=chieuRongTextBoxTabThongTin)
    tbTenHocSinh.place(y=dongHienTaiTabThongTin, x=cotBTabThongTin)
    #sdt hoc sinh
    lblSdtHocSinh = tk.Label(frameThongTinHocSinh, text='SĐT của học sinh:')
    lblSdtHocSinh.place(y=dongHienTaiTabThongTin, x=cotCTabThongTin)
    tbSdtHocSinhText = tk.StringVar()
    tbSdtHocSinh = tk.Entry(frameThongTinHocSinh, textvariable=tbSdtHocSinhText, width=chieuRongTextBoxTabThongTin)
    tbSdtHocSinh.place(y=dongHienTaiTabThongTin, x=cotDTabThongTin)
    dongHienTaiTabThongTin += khoangCachGiua2DongTabThongTin
    #lop cua hoc sinh
    lblLopCuaHocSinh = tk.Label(frameThongTinHocSinh, text='Lớp:')
    lblLopCuaHocSinh.place(y=dongHienTaiTabThongTin, x=cotATabThongTin)
    tbLopCuaHocSinhText = tk.StringVar()
    tbLopCuaHocSinh = tk.Entry(frameThongTinHocSinh, textvariable=tbLopCuaHocSinhText, width=chieuRongTextBoxTabThongTin)
    tbLopCuaHocSinh.place(y=dongHienTaiTabThongTin, x=cotBTabThongTin)
    dongHienTaiTabThongTin += khoangCachGiua2DongTabThongTin
    #hoc phi
    lblHocPhi = tk.Label(frameThongTinHocSinh, text='Học phí:')
    lblHocPhi.place(y=dongHienTaiTabThongTin, x=cotATabThongTin)
    tbHocPhiText = tk.StringVar()
    tbHocPhi = tk.Entry(frameThongTinHocSinh, textvariable=tbHocPhiText, width=chieuRongTextBoxTabThongTin)
    tbHocPhi.place(y=dongHienTaiTabThongTin, x=cotBTabThongTin)
    dongHienTaiTabThongTin += khoangCachGiua2DongTabThongTin
    #ten giao vien
    lblTenGiaoVien = tk.Label(frameThongTinHocSinh, text='Tên giáo viên:')
    lblTenGiaoVien.place(y=dongHienTaiTabThongTin, x=cotATabThongTin)
    chayMySql = MySQL()
    nhanChuoiTenGiaoVien = chayMySql.LayTenGiaoVien()
    cbboxTenGiaoVien = ttk.Combobox(frameThongTinHocSinh, width=22, values=nhanChuoiTenGiaoVien)
    cbboxTenGiaoVien.place(y=dongHienTaiTabThongTin, x=cotBTabThongTin)
    #ma giao vien
    lblMaGiaoVien = tk.Label(frameThongTinHocSinh, text='Mã giáo viên:')
    lblMaGiaoVien.place(y=dongHienTaiTabThongTin, x=cotCTabThongTin)
    print(chayMySql.LayMaGiaoVien('Phạm Như Long'))
    # if cbboxTenGiaoVien.get() != '':
    #     layMaGiaoVien = chayMySql.LayMaGiaoVien(cbboxTenGiaoVien.get())
    #     cbboxMaGiaoVien = ttk.Combobox(frameThongTinHocSinh, width=22, values=layMaGiaoVien)
    #     cbboxMaGiaoVien.place(y=dongHienTaiTabThongTin, x=cotDTabThongTin)
    dongHienTaiTabThongTin += khoangCachGiua2DongTabThongTin
    #nut xac nhan
    btnXacNhanThongTinHocSinh = tk.Button(frameThongTinHocSinh, text='Xác Nhận', command=xacNhanTabThongTin)
    btnXacNhanThongTinHocSinh.place(y=dongHienTaiTabThongTin, x=150)
def tabDanhSachGiaoVien():
    def xacNhanTabGiaoVien():
        noiDungCanTruyenTuTextBox = "'" + \
                                    tbTenGiaoVienText.get() + "','" + \
                                    tbMaGiaoVienText.get() + "'"
        cacCotTrongBangTEACHER = 'TenGV, MaGV'
        tenBang = 'dsgiaovien'
        run = MySQL()
        run.ThemDuLieu(tenBang, noiDungCanTruyenTuTextBox, cacCotTrongBangTEACHER)


    frameDanhSachGiaoVien = tk.Frame(tabControl)
    tabControl.add(frameDanhSachGiaoVien, text='Danh Sách Giáo Viên')
    #tab nhan vien
    dongHienTaiTabGiaoVien = 0
    cotATabGiaoVien = 0
    cotBTabGiaoVien = cotATabGiaoVien + 100
    khoangCachGiua2DongTabGiaoVien = 35
    #ten giao vien
    lblTenGiaoVien = tk.Label(frameDanhSachGiaoVien, text='Tên giáo viên:')
    lblTenGiaoVien.place(y=dongHienTaiTabGiaoVien, x=cotATabGiaoVien)
    tbTenGiaoVienText = tk.StringVar()
    tbTenGiaoVien = tk.Entry(frameDanhSachGiaoVien, textvariable=tbTenGiaoVienText)
    tbTenGiaoVien.place(y=dongHienTaiTabGiaoVien, x=cotBTabGiaoVien)
    dongHienTaiTabGiaoVien += khoangCachGiua2DongTabGiaoVien
    #Ma giao vien
    lblMaGiaovien = tk.Label(frameDanhSachGiaoVien, text='Mã giáo viên:')
    lblMaGiaovien.place(y=dongHienTaiTabGiaoVien, x=cotATabGiaoVien)
    tbMaGiaoVienText = tk.StringVar()
    tbMaGiaoVien = tk.Entry(frameDanhSachGiaoVien, textvariable=tbMaGiaoVienText)
    tbMaGiaoVien.place(y=dongHienTaiTabGiaoVien, x=cotBTabGiaoVien)
    dongHienTaiTabGiaoVien += khoangCachGiua2DongTabGiaoVien
    #nut xac nhan
    btnXacNhanTabGiaoVien = tk.Button(frameDanhSachGiaoVien, text='Xác nhận', command=xacNhanTabGiaoVien)
    btnXacNhanTabGiaoVien.place(y=dongHienTaiTabGiaoVien, x=100)
def tabDanhMucMonHoc():
    def xacNhanTabMonHoc():
        print('chua lamf gif het')
    frameDanhMucMonHoc = tk.Frame(tabControl)
    tabControl.add(frameDanhMucMonHoc, text='Danh Mục Môn học')
    #thiet lap 1 so bien
    dongHienTaiTabMonHoc = 0
    cotATabMonHoc = 0
    cotBTabMonHoc = cotATabMonHoc + 100
    khoangCachGiua2DongTabMonHoc = 35
    #Ten Mon Hoc
    lblTenMonHoc = tk.Label(frameDanhMucMonHoc, text='Tên môn học:')
    lblTenMonHoc.place(y=dongHienTaiTabMonHoc, x=cotATabMonHoc)
    tbTenMonHocText = tk.StringVar()
    tbTenMonHoc = tk.Entry(frameDanhMucMonHoc, textvariable=tbTenMonHocText)
    tbTenMonHoc.place(y=dongHienTaiTabMonHoc, x=cotBTabMonHoc)
    dongHienTaiTabMonHoc += khoangCachGiua2DongTabMonHoc
    #ma mon hoc
    lblMaMonHoc = tk.Label(frameDanhMucMonHoc, text='Mã môn học:')
    lblMaMonHoc.place(y=dongHienTaiTabMonHoc, x= cotATabMonHoc)
    tbMaMonHocText = tk.StringVar()
    tbMaMonHoc = tk.Entry(frameDanhMucMonHoc, textvariable=tbMaMonHocText)
    tbMaMonHoc.place(y=dongHienTaiTabMonHoc, x=cotBTabMonHoc)
    dongHienTaiTabMonHoc += khoangCachGiua2DongTabMonHoc
    #tien to ma nhom
    lblTienToMaNhom = tk.Label(frameDanhMucMonHoc, text='PrefixMaNhom:')
    lblTienToMaNhom.place(y=dongHienTaiTabMonHoc, x= cotATabMonHoc)
    tbTienToMaNhomText = tk.StringVar()
    tbTienToMaNhom = tk.Entry(frameDanhMucMonHoc, textvariable=tbTienToMaNhomText)
    tbTienToMaNhom.place(y=dongHienTaiTabMonHoc, x= cotBTabMonHoc)
    dongHienTaiTabMonHoc += khoangCachGiua2DongTabMonHoc
    #nut xac nhan
    nutXacNhan = tk.Button(frameDanhMucMonHoc, text='Xác Nhận', command=xacNhanTabMonHoc)
    nutXacNhan.place(y=dongHienTaiTabMonHoc, x= 100)
def tabThuHocPhi():
    def xacNhanTabThuHocPhi():
        print('chưa làm gì hết')
    frameThuHocPhi = tk.Frame(tabControl)
    tabControl.add(frameThuHocPhi, text='Thu học phí')
    dongHienTaiTabThuHocPhi = 0
    cotATabThuHocPhi = 0
    cotBTabThuHocPhi = cotATabThuHocPhi + 100
    khoangCachGiua2dong = 35
    #Ma hoc sinh
    lblMaHocSinh = tk.Label(frameThuHocPhi, text='Mã Học Sinh:')
    lblMaHocSinh.place(y=dongHienTaiTabThuHocPhi, x=cotATabThuHocPhi)
    tbMaHocSinhText = tk.StringVar()
    tbMaHocSinh = tk.Entry(frameThuHocPhi, textvariable=tbMaHocSinhText)
    tbMaHocSinh.place(y=dongHienTaiTabThuHocPhi, x=cotBTabThuHocPhi)
    dongHienTaiTabThuHocPhi += khoangCachGiua2dong
    #Ngay dong tien
    lblNgayDongTien = tk.Label(frameThuHocPhi, text='Ngày đóng tiền:')
    lblNgayDongTien.place(y=dongHienTaiTabThuHocPhi, x=cotATabThuHocPhi)
    tbNgayDongTienText = tk.StringVar()
    tbNgayDongTien = tk.Entry(frameThuHocPhi, textvariable=tbNgayDongTienText)
    tbNgayDongTien.place(y=dongHienTaiTabThuHocPhi, x=cotBTabThuHocPhi)
    dongHienTaiTabThuHocPhi += khoangCachGiua2dong
    #nut xac nhan
    btnXacNhan = tk.Button(frameThuHocPhi, text='Xác Nhận', command=xacNhanTabThuHocPhi)
    btnXacNhan.place(y=dongHienTaiTabThuHocPhi, x=100)

if __name__ == '__main__':
    tabThongTin()
    tabDanhSachGiaoVien()
    tabDanhMucMonHoc()
    tabThuHocPhi()
    mainWindow.mainloop()

