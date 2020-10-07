# Write a Python program to calculate the standard deviation of the 
# following data. Go to the editor
# Expected Output :
# Sample Data:  [4, 2, 5, 8, 6]                                                    
# Standard Deviation :  2.23606797749979

import math 

def avg_calc(ls):
    n, mean = len(ls), 0.0
    
    if n <= 1:
        return ls[0]
    
    # calculate average
    for el in ls:
        mean += float(el)
    mean = mean / float(n)
    
    return mean

def sd_data(data):
    n = len(data)
    
    if n <= 1:
        return 0.0
    
    mean, sd = avg_calc(data), 0.0
    
    # calculate standard deviation
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))
    
    return sd

data = [4,2,5,8,6]
print('Sample data: ',data)
print('Standard Deviation: ',sd_data(data))