#Write a Python program to find the first repeated word in a given string.

def fd(strip):
    ck = set()
    for word in strip.split():
        if word in ck:
            return word
        else:
            ck.add(word)
    return False
    
print(fd("ab ca bc ab"))
print(fd("ab ca bc ab ca ab bc"))
print(fd("ab ca bc ca ab bc"))
print(fd("ab ca bc"))