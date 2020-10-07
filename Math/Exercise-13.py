# Write a Python program to find out, if the given number is abundant.
# Note: In number theory, an abundant number or excessive number is a 
# number for which the sum of its proper divisors is greater than the
# number itself. The integer 12 is the first abundant number. Its proper 
# divisors are 1, 2, 3, 4 and 6 for a total of 16.
# Test Data:
# If is_abundant(12)
# If is_abundant(13)
# Expected Output:
# True
# False

def proper_divisors(n):
    result = []
    for i in range(1,n):
        if n % i == 0:
            result.append(i)
    return result

def is_abundant(n):
    s = 0
    for i in range(len(proper_divisors(n))):
        s += proper_divisors(n)[i]
    if s > n:
        return True
    else:
        return False

print(is_abundant(12))
print(is_abundant(13))