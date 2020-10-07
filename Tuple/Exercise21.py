# Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# doi bt 21 <> 22

iplist = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(iplist)
oplist = [l for l in iplist if l]
print(oplist)