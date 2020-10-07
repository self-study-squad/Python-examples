# Write a Python program to get the largest number from a list.

def max_num_in_list(lstip):
    result = lstip[0]
    for i in lstip:
        if result < i:
            result = i
    return result

print(max_num_in_list([1, 2, -8, 0]))