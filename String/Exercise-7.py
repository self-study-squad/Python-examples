#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
#Return the resulting string.
 
def np(ipstr):
    snot = ipstr.find('not')
    spoor = ipstr.find('poor')
    
    if snot < spoor and snot>0 and spoor>0: 
        str1 = ipstr.replace(ipstr[snot:(spoor+4)],'good')
        return str1
    else:
        return ipstr
    
  
 
input_str = input('Input a string: ')
print('String after solving: %s'%np(input_str))