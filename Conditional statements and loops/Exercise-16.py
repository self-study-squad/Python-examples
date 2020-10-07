# Write a Python program to find numbers between 100 and 400 (both included)
# where each digit of a number is an even number. The numbers obtained should be 
# printed in a comma-separated sequence. 

items = []
for i in range(100,401):
    x = str(i)
    if (int(x[0]) % 2 == 0 and int(x[1]) % 2 == 0 and int(x[2]) % 2 == 0):
        items.append(x)
    
print(','.join(items))