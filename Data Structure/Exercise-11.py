# Write a Python program to compare two unordered lists (not sets).
# Expected Output: False

from collections import Counter
def compare_lists(x,y):
    return Counter(x) == Counter(y)

n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
print(compare_lists(n1,n2))