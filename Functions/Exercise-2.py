# Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

def sum_num(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

ip_list = (8,2,3,0,7)
print(sum_num(ip_list))