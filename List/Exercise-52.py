# Write a Python program to compute the similarity between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output: 
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']


from collections import Counter

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

ct1 = Counter(list1)
ct2 = Counter(list2)

print('Missing values in second list: ', list(ct2 - ct1))
print('Missing values in second list: ', list(ct1 - ct2))