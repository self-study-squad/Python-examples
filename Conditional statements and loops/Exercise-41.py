# Write a Python program to get next day of a given date.
# Expected Output:

# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24   


def check_last_date(x,y:int):
    if (x == 31) or (x == 30 and (y == 4 or y == 6 or y == 9 or y == 11)) or (((x == 29) or (x == 28)) and y == 2):
        return True
    return False

year = int(input('Input a year: '))
month = int(input('Input a month [1-12]:'))
day = int(input('Input a day [1-31]:'))
nmonth = nyear = nday = 0
if check_last_date(day,month):
    if month == 12:
        nday = 1
        nyear = year + 1
        nmonth = 1
    else:
        nday = 1
        nyear = year
        nmonth = month + 1
else:
    nday = day + 1
    nmonth = month
    nyear = year

print('The next date is [yyyy-mm-dd] ' + str(nyear) + '-' + str(nmonth) + '-' + str(nday))   