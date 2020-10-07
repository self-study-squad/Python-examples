#Write a Python program to count the number 4 in a given list.

def count4(nlist):
    i=0
    for j in range(len(nlist)-1):
        if nlist[j]=='4':
            i += 1
    return i

num_list = list(input('Input list seperate by comma: '))
print('There is/are %2d number(s) 4 in the list!'%(count4(num_list)))