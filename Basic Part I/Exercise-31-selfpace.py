# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x,y):
    t = min(x,y)
    while t>0:
        if (x % t == 0) and (y % t == 0):
            result = t
            break;
        t -= 1
    return t

print(gcd(336,360))