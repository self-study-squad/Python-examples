# Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

from itertools import tee, chain, zip_longest
def replace2copy(listip):
    list1, list2 = tee(iter(listip),2)
    return list(chain.from_iterable(zip_longest(listip[1::2],listip[::2])))

n=[0,1,2,3,4,5]
print(replace2copy(n))