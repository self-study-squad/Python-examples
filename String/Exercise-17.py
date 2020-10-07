#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#Sample function and result :
#insert_end('Python') -> onononon
#insert_end('Exercises') -> eseseses

def insert_end(strip):
    result = strip[-2:]*4
    return result

print(insert_end('Python'))
print(insert_end('Exercises'))