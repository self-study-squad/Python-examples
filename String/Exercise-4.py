# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

input_str = input('Nhập chuỗi: ')

char = input_str[0]
sol_str = input_str[1:len(input_str)]
input_str = sol_str.replace(char,'$')
output_str = char + input_str
print('Chuỗi sau khi xử lý: %s'%output_str)
