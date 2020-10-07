# Write a Python program that accepts a string and calculate the number of digits and 
# letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6 
# Digits 2

strip = input('Input a string: ')
digits = 0
letters = 0
for p in strip:
    if p.isdigit():
        digits += 1
    if p.isalpha():
        letters += 1

print('Digits: ', digits, ', Letters: ', letters)