from math import pi
r = float(input('Nhap ban kinh: '))
list = (r, 2*r*pi, pi*r**2)
print('Duong tron ban kinh %5d co chu vi %8.2f , dien tich la %8.2f .'% (r,list[1],list[2]))