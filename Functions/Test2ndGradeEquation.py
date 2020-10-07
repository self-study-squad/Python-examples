#Giai phuong trinh bac 2

from math import sqrt

a=int(input('Nhap a:'))
b=int(input('Nhap b:'))
c=int(input('Nhap c:'))

if (a==0):
    if(b==0):
        if(c==0):
            print('Phương trình có vô số nghiệm!')
        else:
            print('Phương trình vô nghiệm!')
    else:
        print('Phương trình có nghiệm duy nhất: x=%f'%(-b/(2*a)))
else:
    delta = b**2-4*a*c
    if (delta>0):
        print('Phương trình có hai nghiệm phân biệt: ')
        print('x1=%f'%((-b+sqrt(delta))/(2*a)))
        print('x2=%f'%((-b-sqrt(delta))/(2*a)))
    elif(delta==0):
        print('Phương trình có nghiệm kép x= %f'%(-b/(2*a)))
    else:
        print('Phương trình vô nghiệm!')
