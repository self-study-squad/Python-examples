# Write a Python program to calculate the difference between the squared sum of
# first n natural numbers and the sum of squared first n natural numbers.
# (default value of number=2).

# Test Data:
# If sum_difference(12)
# Expected Output :
# 5434 

def sum_square(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_square(n-1)
    
def square_sum(n):
    result = 0
    for i in range(n+1):
        result += i
    result **= 2
    return result


def sum_difference(n):
    return abs(square_sum(n) - sum_square(n))

k = int(input('Input n: '))
print(sum_difference(k))