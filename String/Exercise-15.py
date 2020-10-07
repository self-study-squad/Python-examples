# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
#add_tags('i', 'Python') -> '<i>Python</i>'
#add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def hashtag(tg,strip):
    result = '<' + tg + '>' + strip + '</' + tg + '>'
    return result

stringip = input('Input the string: ')
tag = input('Input the tag: ')
print('The HTML code with tag and string: %s'%hashtag(tag,stringip))