#Write a Python program to count the occurrences of each word in a given sentence.
def countwords(strip):
    counts = dict()
    words = strip.split()
    for word in words:
        if word in counts: 
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

stringip = input('Input a string: ')
print('String after process: ')
print(countwords(stringip))