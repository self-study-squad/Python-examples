# Write a Python function that checks whether a passed string is palindrome or not. 
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as 
# forward, e.g., madam or nurses run.

inputstring = input('Input a string: ')
if inputstring == inputstring[::-1]:
    print(inputstring + ' is a palindrom string.')
else:
    print(inputstring + ' is not a palindrom string.')