#Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.

def fd(strip):
    dt = {}
    for i in strip:
        if i in dt:
            return i
            break
        else:
            dt[i] = 1
    return None

print(fd('abcabc'))
print(fd('abbcabc'))
print(fd('abcbabc'))
print(fd('abcxxy'))
print(fd('abc'))
