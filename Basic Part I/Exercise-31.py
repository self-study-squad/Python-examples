# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x,y):
    str_gcd = ''
    no = -1
    
    min_num = min(x,y)
    for i in range(1,min_num):
        if (x % i == 0) and (y % i == 0): 
            str_gcd += str(i) + ','
    st = str_gcd[:-1]
    str_gcd = st
    gcd = str_gcd.split(',')
    t = gcd[len(gcd)-1]
    return t

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))
print('The Greatest Common Divisor is: %s'%(gcd(num1,num2)))
    
    