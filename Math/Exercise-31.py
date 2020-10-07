# Write a Python program to convert a decimal number to binary number. 
# Expected Output :
# Input a binary number: 101011                                           
# The decimal value of the number is 43

b_num = list(input('Input a binary number: '))
value = 0

for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2,i)
        
print('The decimal value of the number is: ',value)