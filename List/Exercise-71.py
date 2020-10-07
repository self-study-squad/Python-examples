# Write a Python program to check if all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list1 = [{},{},{}]
list2 = [{1,2},{},{}]

print(all(not d for d in list1))
print(all(not d for d in list2))