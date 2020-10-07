# Write a Python program to sort a list of elements using the selection sort algorithm. 
# Note : The selection sort improves on the bubble sort by making only one exchange for 
# every pass through the list. 
# Sample Data: [14,46,43,27,57,41,45,21,70]
# Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]

def SelectionSort(listip):
    for maxpos in range(len(listip)-1,0,-1):
        cgpos = 0
        for pos in range(1, maxpos+1):
            if listip[pos]>listip[cgpos]:
                cgpos = pos
        temp = listip[cgpos]
        listip[cgpos] = listip[maxpos]
        listip[maxpos] = temp


nlist = [14,46,43,27,57,41,45,21,70]
SelectionSort(nlist)
print(nlist)