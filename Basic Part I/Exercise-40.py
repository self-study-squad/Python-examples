#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math

def cal(x_1,y_1,x_2,y_2):
    result = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    return result

a = float(input('Input first M(a,b) - a = : '))
b = float(input('Input second M(a,b) - b = : '))
c = float(input('Input first N(c,d) - c = : '))
d = float(input('Input second N(c,d) - d = : '))

print(cal(a,b,c,d))
