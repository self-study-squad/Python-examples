# Write a Python program to combine values in python list of dictionaries
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

from collections import Counter

list_of_dic = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()
for d in list_of_dic:
    result[d['item']] += d['amount']

print(result)