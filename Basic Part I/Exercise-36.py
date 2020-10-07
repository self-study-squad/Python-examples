#Write a Python program to add two objects if both objects are an integer type.

def checknum(x,y):
    if not((isinstance(x,int)) and (isinstance(y,int))):
        raise TypeError('Inputs must be both in Integer')
    return x + y

print(checknum(10,20))
