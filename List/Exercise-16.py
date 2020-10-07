# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

listop = []

for i in range(1,21):
    x = i**2
    listop.append(x)

print(listop[:5])
print(listop[-5:])