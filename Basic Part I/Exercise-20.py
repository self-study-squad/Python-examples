#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def rpstr(text,num):
    s=''
    for i in range(num):
        s=s+text
    return s

str_input = input('Input the string: ')
times = int(input('Input the repeat times: '))
print('Handled strings: %s'%(rpstr(str_input,times)))