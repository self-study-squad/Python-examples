# Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from collections import Counter

ipdict = {'Math':81, 'Physics':83, 'Chemistry':87}

x = Counter(ipdict)
print(x.most_common())
print(type(x))

y = Counter('aabbbcccccccc')
print(type(y))
print(y.most_common())
print(type(y))
