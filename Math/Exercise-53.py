# Write a Python program to flip a coin 10000 times and count heads 
# and tails. Go to the editor
# Expected Output :
# Heads: 5073
# Tails: 4927 

import random
import itertools

result = {
    'heads': 0, 
    'tails': 0,
    }

sides = list(result.keys())

for i in range(10000):
    result[random.choice(sides)] += 1

print('Heads: ',result['heads'])
print('Tails: ',result['tails'])