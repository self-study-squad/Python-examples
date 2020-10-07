# Write a Python program to find the list of words that are longer than n from a given list of words.

def long_words(n,strip):
    lstip = strip.split(' ')
    lstop =[]
    for x in lstip:
        if len(x)>n: 
            lstop.append(x)
    return lstop




print(long_words(3, "The quick brown fox jumps over the lazy dog"))