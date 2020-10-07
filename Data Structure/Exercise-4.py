# Write a Python program to get all values from an enum class.
# Expected output:
# [93, 355, 213, 376, 244, 672]

import enum

class Countries(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

country_code_list = list(map(int, Countries))
print(country_code_list)