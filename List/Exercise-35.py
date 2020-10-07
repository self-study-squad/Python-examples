# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

my_list = ['p', 'q']
n = 4

newlist =['{}{}'.format(x,y) for y in range(1,n+1) for x in my_list]
print(newlist)