#Write a Python program to test whether a passed letter is a vowel or not.

tup_vowels = ['a','e','i','o','u']

def check(lt):
    s = set(tup_vowels)
    if lt in s:
        return True
    else: 
        return False

letter = input('Input a letter to check: ')
if check(letter):
    print('Input letter is a Vowel')
else:
    print('Input letter is a Consonant')