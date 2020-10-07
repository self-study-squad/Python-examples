# Write a Python program for sequential search. 
# Sequential Search : In computer science, linear search or sequential search is 
# a method for finding a particular value in a list that checks each element in 
# sequence until the desired element is found or the list is exhausted. 
# The list need not be ordered.
# Test Data :
# Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3) 

def Sequential_Search(listip,item):
    i = 0 
    found = False
    while (i <= len(listip) and not found):
        if listip[i] == item:
            found = True
            break
        else:
            i += 1
    return found, i




print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))