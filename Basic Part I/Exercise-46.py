#Write a python program to get the path and name of the file that is currently executing. 

import os

print('Current execute files: ',os.path.realpath(__doc__))