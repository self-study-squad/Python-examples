# Write a Python program to create a shallow copy of sets. Go to the editor

# Note : Shallow copy is a bit-wise copy of an object. 
# A new object is created that has an exact copy of the values in the original object.

setp = set(['red','green'])
setq = set(['green','red'])

# A shallow copy
setr = setp.copy()
print(setr)