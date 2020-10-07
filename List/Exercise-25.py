# Write a python program to select an item randomly from a list.

import random

color_list = ['Black','Blue','Green','White','Red','Yellow']

print(random.choices(color_list,k=2))