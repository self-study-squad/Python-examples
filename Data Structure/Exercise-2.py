# Write a Python program to iterate over an enum class and display individual member and
# their value.
# Expected Output:
# Afghanistan = 93
# Albania = 355
# Algeria = 213
# Andorra = 376
# Angola = 244
# Antarctica = 672

from enum import Enum

class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in Countries:
    print('{:15} = {}'.format(data.name,data.value))