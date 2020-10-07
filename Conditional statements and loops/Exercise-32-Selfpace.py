# Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.


vowels = 'aeiou'
ltt = input('Input a letter of the alphabet: ')
t = vowels.find(ltt)
if t == -1:
    print(ltt + ' is not a vowel!')
else:
    print(ltt + ' is a vowel')