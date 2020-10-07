# Write a Python program to calculate the value of 'a' to the power 'b'.
# Test Data : 
# (power(3,4) -> 81 

def power(a,b):
    if b <= 0:
        return 1
    else:
        return a * pow(a,b-1)

print(power(3,4))