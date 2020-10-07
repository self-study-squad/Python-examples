# Write a Python program to find the second largest number in a list. 

list1 = [-8,1,2,-2,0]
list2 = [1,1,0,0,2,-2,-2]
list3 = [1,-1,0,-9,4,-5]
list4 = [1,4,0,23,6,34]

def sln(listinput):
    resort_set = set()
    resort_list = []
    for x in listinput:
        if x not in resort_set:
            resort_set.add(x)
            resort_list.append(x)
    resort_list.sort()
    resort_list.reverse()
    if len(resort_list) < 1:
        return NONE
    else:
        return resort_list

print(sln(list1)[1])
print(sln(list2)[1])
print(sln(list3)[1])
print(sln(list4)[1])
print(sln([2,2]))

