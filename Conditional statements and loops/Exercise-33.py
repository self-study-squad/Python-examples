# Write a Python program to convert month name to a number of days. Go to the editor
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 

month_dict ={'January':1, 'February':2, 'March':3, 'April':4,'May':5,'June':6,'July':7,'August':8,'September':9, 'October':10,'November':11, 'December':12}
date_list = ('31','28','31','30','31','30','31','31','30','31','30','31')
alter = '29'

month_input = input('Please input the name of the Month: ')
if month_input == 'February':
    print('%s days'%(date_list[1] + '/' + alter))
else:
    print('%s days'%(date_list[month_dict[month_input]-1]))
    