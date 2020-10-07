# Write a Python program to iterate over two lists simultaneously.

num = [1,2,3]
color = ['red','blue','green']

for n,c in zip(num,color):
    print(n,c)

