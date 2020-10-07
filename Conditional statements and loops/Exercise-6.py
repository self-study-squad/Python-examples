# Write a python program to count the number of even and odd numbers 
# from a series of odd numbers.
# Sample numbers: nums = (1,2,3,4,5,6,7,8,9)
# Expected Output: 
# Number of even numbers: 5
# Number of odd numbers: 4

nums = (1,2,3,4,5,6,7,8,9)
even, odd = 0,0

for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('Number of even numbers: ',even)
print('Number of odd numbers: ',odd)
