#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

ipstr = input('Input comma seperate words: ')
strlist = [word for word in ipstr.split(',')]
print(','.join(sorted(list(set(strlist)))))