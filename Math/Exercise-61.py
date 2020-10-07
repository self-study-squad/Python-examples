# Write a Python program to describe linear regression. 
# Note : A linear regression line has an equation of the 
# form Y = a + bX, where X is the explanatory variable and Y 
# is the dependent variable. The slope of the line is b, and a 
# is the intercept (the value of y when x = 0).
# Expected Output :
# Enter the number of data points: 2                    
# X1: 1  
# Y1: 2 
# X2: 3    
# Y2: 4  
# Best fit line:
# y = 1.0x + 1.0
# Enter a value to calculate: 12                            
# y = 13.0 

# Define the data
data = set()
count = int(input('Enter the number of data points: '))
for i in range(count):
    x = float(input('Input an x: '))
    y = float(input('Input an y: '))
    data.add((x,y))
    
# Find the average x and y
avgx = avgy = 0.0

for i in data:
    avgx += i[0]/len(data)
    avgy += i[1]/len(data)
    
# Find the sums
totalx = totaly = 0
for i in data:
    totalx += (i[0] -avgx)**2
    totaly += (i[0]-avgx)*(i[1]-avgy)
    
m = totalx / totaly
b = avgy - m*avgx

print('Best fit line: ')
print('y= '+str(m)+'x + '+ str(b))

x = float(input('Enter a value to calculate: '))
print('y= '+str(m*x+b))