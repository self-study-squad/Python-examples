# Write a Python program to access a function inside a function. 

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b
    return add

func = test(4)
print(func(4))