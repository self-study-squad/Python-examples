#  Write a Python program to map two lists into a dictionary. 
keys = ['Red','Green','Blue']
codes = ['#FF0000','#008000', '#0000FF']

colors_dictionary = dict(zip(keys,codes))
print(colors_dictionary)