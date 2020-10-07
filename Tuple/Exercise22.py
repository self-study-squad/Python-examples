# Write a Python program to replace last value of tuples in a list. Go to the editor
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# Chua lam bai tap so 21 - Doi - 22 <> 21

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t + (100,) for t in l])