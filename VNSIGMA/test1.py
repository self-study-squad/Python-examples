import math
a = int(input())
b = int(input())
c = int(input())

def ptb2(x,y,z:int):
    delta = y**2 -4*x*z
    if delta < 0:
        return False
    elif delta >= 0:
        x1 = (-y + math.sqrt(delta))/(2*x)
        x2 = (-y - math.sqrt(delta))/(2*x)
        return x1, x2

def countpos(x,y:int):
    if x>0 and y>0:
        return 2
    elif x>0 and y<0:
        return 1
    elif x<0 and y<0:
        return 0

s = 0
if ptb2(a,b,c) != False:
    p,q = ptb2(a,b,c)
    s = countpos(p,q)
    if p != 0 and q != 0:
        s *= 2
    else:
        s *= 2
        s -= 1
print(s)
