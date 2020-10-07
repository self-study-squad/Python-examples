# Write a Python program to print a random sample of words from 
# the system dictionary. Go to the editor
# Expected Output :
# cellophane's                                            
# matter's                                                       
# Whiteley's                                                     
# airdrop's                                                      
# sulkiest                                                       
# whisper's                                                      
# downturns 

import random
with open('/usr/share/dict/words','rt') as fh:
    words = fh.readlines()
words = [w.rstrip() for w in words]
for w in random.sample(words,7):
    print(w)