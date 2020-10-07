# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336 

def mul_num(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

ip_list = (8, 2, 3, -1, 7)
print(mul_num(ip_list))