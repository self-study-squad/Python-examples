# Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.

l = input('Input a letter of the alphabet: ')

if l in ('a','e','i','o','u'):
    print('%s is a vowel.'%l)
elif l == 'y':
    print('Sometimes letter y stand for vowel, sometimes stand for consonant.')
else:
    print('%s is a consonant.'%l)