#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sol(a,b,c):
    if a==b==c:
        return 9*a
    else:
        return a+b+c
print(sol(2,3,5))
print(sol(5,5,5))
print(sol(2,2,2))
print(sol(3,1,9))