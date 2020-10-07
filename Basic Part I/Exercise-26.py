#Write a Python program to create a histogram from a given list of integers.

def draw(count,chardr):
    output = ''
    while count > 0:
        output += chardr + ' '
        count -= 1
    return output

pr_char = input('Input the chart to plot: ')
liststr = input('Input the list time, seperate by comma: ')
list_times = liststr.split(',')
t = 0
while t < len(list_times):
    print(draw(int(list_times[t]),pr_char))
    t += 1