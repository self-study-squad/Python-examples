# Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8]

def peven(x:list):
    result = []
    for i in x:
        if (result.count(i) == 0) and (i % 2 == 0):
            result.append(i)
    return result

print(peven([1,2,3,4,5,6,7,8,9]))