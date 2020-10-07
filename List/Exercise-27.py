# Write a Python program to find the second smallest number in a list.

list1 = [-8,1,2,-2,0]
list2 = [1,1,0,0,2,-2,-2]
list3 = [1,-1,0,-9,4,-5]
list4 = [1,4,0,23,6,34]

def smn(list_input):
    dumplicate_sort = set()
    resort_list = []
    for x in list_input:
        if x not in dumplicate_sort:
            dumplicate_sort.add(x)
            resort_list.append(x)
    resort_list.sort()
    return resort_list

print(smn(list1))
print(smn(list1)[1])
print(smn(list2))
print(smn(list2)[1])
print(smn(list3))
print(smn(list3)[1])
print(smn(list4))
print(smn(list4)[1])