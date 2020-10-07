#Write a Python program to find the second most repeated word in a given string.

def words(strip):
    ctstrip = strip.split()
    dicstr = {}
    for word in ctstrip:
        if word in dicstr:
            dicstr[word] += 1
        else:
            dicstr[word] = 1 
    dicstr = sorted(dicstr.items(), key=lambda kv: kv[1])
    return dicstr[-2]
    

        





stringip = "Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."
print(words(stringip))