# Write a Python program to parse math formulas and put parentheses 
# around multiplication and division. Go to the editor
# Sample data : 4+5*7/2
# Expected Output :
# 4+((5*7)/2)

import ast

def recurse(node):
    if isinstance(node,ast.BinOp):
        if isinstance(node.op, ast.Mult) or isinstance(node.op,ast.div):
            print('('.end='')
            recurse(node.left)
            recurse(node.op)
            recurse(node.right)