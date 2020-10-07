# Write a Python program to calculate the sum of all digits of the base
# to the specified power.

# Test Data:
# If power_base_sum(2, 100)
# Expected Output :
# 115

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])


print(power_base_sum(2, 100))
print(power_base_sum(8, 10))
