#Write a Python program to count and display the vowels of a given text.

vowels = 'aeiou'

strip = input('Input a string: ')

ct = 0
for i in strip:
    if i in vowels:
        ct += 1
        print(i)
print(ct)