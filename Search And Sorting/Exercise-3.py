# Write a Python program for binary search for an ordered list.
# Test Data :
# Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
# Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False 

def Binarysort(listip,item):
    found = False
    low = 0
    high = len(listip)-1
    mid = (low + high)//2
    while (not found and low <= high):
        if (item in (listip[low], listip[high], listip[mid])):
            found = True
        elif listip[mid] < item:
            low = mid + 1
            mid = (low + high)//2
        elif listip[mid] > item:
            high = mid - 1 
            mid = (low + high)//2
    return found
    
    
    
    
print(Binarysort([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(Binarysort([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))