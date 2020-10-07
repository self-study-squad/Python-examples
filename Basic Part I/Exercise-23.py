#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 

def sol(num,givenstring):
    result = givenstring
    if len(givenstring)<2:
        for i in range(num - 1):
            result +=givenstring
    else:
        result = givenstring[:2]
        for i in range(num - 1):
            result += givenstring[:2]
    return result

pro_string = input('Input the given string: ')
rep_times = int(input('Input the repeat times: '))
print('String after handling: %s'%(sol(rep_times,pro_string)))