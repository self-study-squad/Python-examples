# Write a Python program to returns sum of all divisors of a number. 
# Test Data:
# If number = 8
# If number = 12
# Expected Output:
# [1, 2, 4]
# [1, 2, 3, 4, 6] 

def sum_div(n):
    result = []
    for i in range(1,n):
        if n % i == 0:
            result.append(i)
    return result

print(sum_div(8))
print(sum_div(12))