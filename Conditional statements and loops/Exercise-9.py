# Write a Python program to get a fibonacci Sequence between 0 to 50.
'''
def fib(x:int):
    if (x == 1 or x == 2):
        return 1
    else:
        return fib(x-1) + fib(x-2)

for i in range(0,50):
    print(fib(i))
    '''
x, y = 1,1
print(x)
t = 1
while t <= 50:
    t += 1
    print(y)
    x, y = y, x+y
    