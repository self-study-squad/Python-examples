# Write a Python program that reads two integers representing a month and day and prints 
# the season for that month and day. Go to the editor
# Expected Output:

# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn  

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
    season = 'winter'
elif month in ('April', 'May', 'June'):
    season = 'spring'
elif month in ('July', 'August', 'September'):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season = 'summer'
elif (month == 'September') and (day > 21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'

print("Season is",season)