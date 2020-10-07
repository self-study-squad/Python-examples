# Write a Python program to multiply all the items in a dictionary.

d = {'data1': 100,'data2':-54, 'data3':247}
result = 1
for i in d:
    result *= d[i]
print(result)