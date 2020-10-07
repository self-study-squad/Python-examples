# Write a python program that accept words from users and reverse it

# word = input('Input a word to reverse: ')

# for char in range(len(word)-1,-1,-1):
#     print(word[char],end='')
# print('\n')

words = input('Input a word to reverse: ')

t = len(words)-1
while (t >= 0):
  print(words[t],end='')
  t -= 1
