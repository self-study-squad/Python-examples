import sqlite3

path = "E:\My Usage\Python\KVDatabase\KVDatabase.db"
db = sqlite3.connect(path)

n=int(input("Nhập số học sinh cần thêm mới: "))
while n>0:
    ten=input("Tên học sinh: ")
    ngayvaohoc=input("Ngày vào học: ")
    lopbd=int(input("Lớp bắt đầu: "))
    tths=input("Tình trạng (Đang học/Đã nghỉ): ")
    
    DataTuple=(ten,ngayvaohoc,lopbd,tths)
    sqliteparam="INSERT INTO DanhsachHS(Tenhs,Ngayvaohoc,Lopbatdau,TinhTrangHS) VALUES(?,?,?,?);"
    db.execute(sqliteparam,DataTuple)
    n -= 1

db.commit()
print(db.execute("SELECT * FROM DanhsachHS;"))