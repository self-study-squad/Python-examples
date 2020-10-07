#  Write a Python function that takes a list and returns a new list with unique elements 
# of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def sortlist(x):
    result = []
    for i in x:
        if result.count(i) == 0:
            result.append(i)
    return result


print(sortlist([1,2,3,3,3,3,3,3,4,5]))