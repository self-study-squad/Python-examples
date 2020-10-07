# Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output: 
# item4 55
# item1 45.5
# item3 41.3




from heapq import nlargest
from operator import itemgetter


itemsip = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24} 

for name, value in nlargest(3, itemsip.items(), key=itemgetter(1)):
    print(name, value)

#for name, val in nlargest(3,itemsip.keys(), key=itemgetter(1)):
 #   print(name, val)