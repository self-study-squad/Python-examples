# Write a Python program to print alphabet pattern 'D'. Go to the editor
# Expected Output:

 # ****                                                                   
 # *   *                                                                  
 # *   *                                                                  
 # *   *                                                                  
 # *   *                                                                  
 # *   *                                                                  
 # **** 
 
for i in range(0,7):
    if i in range(1,6):
        print(' *   *')
    else:
        print(' ****')