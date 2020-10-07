# Write a Python program to compute sum of digits of a given string.

def sum_digits_string(strip):
    sumdigit = 0
    for z in strip:
        if z.isdigit() == True:
            sumdigit += int(z)
    return sumdigit




print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))