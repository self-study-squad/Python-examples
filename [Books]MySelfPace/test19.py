# Thread

import time

def cal_square(numbers):
    print('Calc square numbers: ')
    for i in numbers:
        print('Square %d: %d'%(i,i*i))
  
def cal_cube(numbers):
    print('Cal cube numbers: ')
    for i in numbers:
        print('Cube %d: %d'%(i,i*i*i))

t=time.time()
arr=[2,4,6,8]
cal_square(arr)
cal_cube(arr)
print('Time consumed: ',time.time()-t)

print('Another way with threading for comparition:')

import threading
from threading import Thread

t=time.time()
t1 = threading.Thread(target=cal_square,args=(arr,))
t2 = threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Time consumed: ',time.time()-t)