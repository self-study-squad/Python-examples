# Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

def mod7(x:int):
    if x % 7 == 0:
        return True
    return False

def mul5(x:int):
    if x % 5 == 0:
        return True
    return False

def sol(x,y:int):
    for i in range(x,y):
        if mod7(i) and mul5(i):
            print(i)

sol(1500,2701)