# Write a Python program to find the index of an item of a tuple.

# Create a tuple
tuplex = tuple('index tuple')
print(tuplex)

# Get index of the first item whose value is passed as parameter
index = tuplex.index('t')
print(index)

# define the index from which you want to search
index = tuplex.index('e',6)
print(index)

# define the segment of the tuple to be searched
index = tuplex.index('e',1,8)
print(index)

# if item not exists in the tuple return ValueError Exception
# index = tuplex.index('y')