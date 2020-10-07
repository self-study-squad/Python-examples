# Write a Python program to get the sum of a non-negative integer.
# Test Data: 
# sumDigits(345) -> 12
# sumDigits(45) -> 9 

def sumDigits(n):
    if n < 1:
        return 0
    else:
        return n%10 + sumDigits(n//10)

k = int(input('Input a number: '))
print('Sum all digits = '+ str(sumDigits(k)))