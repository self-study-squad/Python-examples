# Write a Python program to multiplies all the items in a list.

def multiply_list(lstip):
    result = 1
    for i in lstip:
        result *= i
    return result

print(multiply_list([1,2,-8]))