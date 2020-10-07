# Write a Python program to count the number of elements in a list within a specified range. 


list1 = [10,20,30,40,40,40,70,80,99]
list2 = ['a','b','c','d','e','f']

def ct(li,min,max):
    result =0
    for x in li:
        if min <= x <= max:
            result += 1
    return result


print(ct(list1,40,100))
print(ct(list2,'a','e'))
    