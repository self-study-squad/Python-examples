# Write a Python program to construct the following pattern, using a nested loop number. 
# Expected Output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(1,10):
    t = i
    while t>0:
        print(i,end='')
        t -= 1
    print()
