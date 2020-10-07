# Write a Python program of recursion list sum. 

def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total += recursive_list_sum(element)
        else:
            total += element
    return total

print(recursive_list_sum([1,2,[3,4],[5,6]]))