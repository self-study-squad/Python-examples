# Write a Python program to swap comma and dot in a string. Go to the editor
#Sample string: "32.054,23"
#Expected Output: "32,054.23"

strip = '32.054,23'

maketrans = strip.maketrans
strip = strip.translate(maketrans(',.', '.,'))
print(strip)

'''amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)'''