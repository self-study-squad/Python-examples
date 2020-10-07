# Write a Python program to compute the similarity between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output: 
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

sdif12 = set(color1) - set(color2)
ldif12 = list(sdif12)
print('color1 - color2: ' + str(ldif12))

sdif21 = set(color2) - set(color1)
ldif21 = list(sdif21)
print('color2 - color1: ' + str(sdif21))
