# Write a Python program to sum all amicable numbers from 1 to specified numbers. 
# Note: Amicable numbers are two different numbers so related that the sum of the 
# proper divisors of each is equal to the other number. (A proper divisor of a 
# number is a positive factor of that number other than the number itself.
# For example, the proper divisors of 6 are 1, 2, and 3.)

# Test Data:
# If amicable_numbers_sum(9999)
# If amicable_numbers_sum(999)
# If amicable_numbers_sum(99)
# Expected Output:
# 31626
# 504
# 0 

def sum_proper_divisor(n):
    t = 0
    for i in range(1,n):
        if n % i == 0:
            t += i
    return t

def sum_amicable_numbers(n):
    result = 0
    i = 0
    while i<n:
        i += 1
        for j in range(i+1,n):
            if (sum_proper_divisor(i) == j) and (sum_proper_divisor(j) == i):
                result += i
                result += j
    return result

print(sum_amicable_numbers(9999))
print(sum_amicable_numbers(999))
print(sum_amicable_numbers(99)) 
