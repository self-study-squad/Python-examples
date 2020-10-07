# Write a Python program to calculate the sum of a list of numbers.

def list_sum(listip):
    result = 0
    for i in listip:
        result += i
    return result

print(list_sum([2, 4, 5, 6, 7]))