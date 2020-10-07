# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

listip = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def change_list(lstip):
    result = [t for (i,t) in enumerate(lstip) if i not in (0,4,5)]
    return result


print(change_list(listip))