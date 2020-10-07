# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def swap(strip):
    first = strip[0]
    last = strip[-1]
    result = strip[1:(len(strip)-1)]
    result = last + result + first
    return result

stringip = input('Input a string: ')
print('The string after procedure: %s'%swap(stringip))