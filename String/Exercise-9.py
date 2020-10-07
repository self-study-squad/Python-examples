#Write a Python program to remove the nth index character from a nonempty string

def remove_char(strip,charno):
    result = strip[:(charno-1)] + strip[charno+1:]
    return result
ipstr = input('Input a string: ')
no = int(input('Input the destination number of the string to delete: '))
print('The output string will be: %s'%remove_char(ipstr,no))