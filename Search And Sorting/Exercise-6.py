# Write a Python program to sort a list of elements using the insertion sort algorithm.
# Note : According to Wikipedia "Insertion sort is a simple sorting algorithm that builds
# the final sorted array (or list) one item at a time. It is much less efficient on 
# large lists than more advanced algorithms such as quicksort, heapsort, or merge sort."
# Sample Data: [14,46,43,27,57,41,45,21,70]
# Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]


def InsertionSort(listip):
    for index in range(1, len(listip)):
        
        currentvalue = listip[index]
        position = index
        
        while position > 0 and listip[position - 1] > currentvalue:
            listip[position] = listip[position - 1]
            position = position - 1
            
        listip[position] = currentvalue
        
        

nlist = [14,46,43,27,57,41,45,21,70]
InsertionSort(nlist)
print(nlist)