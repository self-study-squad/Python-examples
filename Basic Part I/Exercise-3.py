import datetime
now = datetime.datetime.now()
print('Current date & time : ',end='')
print(now.strftime("%Y-%m-%d %H:%M:%S"))
