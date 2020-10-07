#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

pri_amount = float(input('Input the principal amount: '))
rate = float(input('Input the rate of interest: '))
year = float(input('Input the number of years to calculate: '))

result = pri_amount*(1+rate*0.01)**year
print('The amount you will get after %6.2f years will be: %6.2f'%(year,result))