def string_len(str):
    count = 0
    for t in str:
        count += 1
    return count

ip_string = input('Input a string: ')
print('Length of the input string is: %3d'%string_len(ip_string))
print('Length of the string calculate by Python function is: %3d'%len(ip_string))