# Write a Python program for binary search. 
# Binary Search : In computer science, a binary search or half-interval search algorithm 
# finds the position of a target value within a sorted array. The binary search algorithm 
# can be classified as a dichotomies divide-and-conquer search algorithm and executes in 
# logarithmic time.

def search(listip, item):
    found = False
    low = 0
    high = len(listip)-1
    mid = (low + high)//2
    while (low <= high and not found):
        if (listip[low] == item) or (listip[high]==item) or (listip[mid]==item):
            found = True
            break
        elif listip[low] < item:
            low = mid + 1
            mid = (low + high)//2
        elif listip[high] > item:
            high = mid - 1
            mid = (low + high)//2
    return found

print(search([6,12,17,23,38,45,77,84,90],45))
print(search([1,2,3,5,8],6))
print(search([1,2,3,5,8],5))