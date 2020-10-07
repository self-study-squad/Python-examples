import sqlite3
path = "E:\My Usage\Python\KVDatabase\KVDatabase.db"
conn = sqlite3.connect(path)
print("Connect sucessfully!!!")

cursor = conn.execute("SELECT DanhSachHS.Tenhs,DMMonHoc.TenMonHoc,DSGiaoVien.TenGV FROM DanhSachHS INNER JOIN HSTheoNhom ON DanhSachHS.Mahs = HSTheoNhom.Mahs INNER JOIN DSNhom ON HSTheoNhom.MaNhom = DSNhom.MaNhom INNER JOIN DSGiaoVien ON DSNhom.MaGV = DSGiaoVien.MaGV INNER JOIN DMMonHoc ON DSNhom.MaMonHoc=DMMonHoc.MaMonHoc")

for row in cursor:
    print('Mã giáo viên: ',row[0],'; Tên giáo viên: ',row[2])

cursor = conn.execute()
conn.close()