# Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. 
# After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73

def cal_age(x:int):
    if x == 1:
        return 10.5
    elif x == 2:
        return 21
    else:
        return cal_age(x-1) + 4

human_years = input('Input a dog\'s in human years: ')
print('The dog\'s age in dog\'s years is '+str(cal_age(15)))