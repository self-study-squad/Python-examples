#Write a Python program to count and display the vowels of a given text.

def vowels(text):
    vowels = 'aeiouAEIOU'
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
vowels('w3resource.com');