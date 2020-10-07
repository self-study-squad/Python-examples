import threading
import time

def deamon():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(),'Exiting')


def nondeamon():
    print(threading.currentThread().getName(),'Starting')
    print(threading.currentThread().getName(),'Exiting')

d = threading.Thread(name='deamon',target=deamon)
d.setDaemon(True)
t = threading.Thread(name=nondeamon,target=nondeamon)

d.start()
t.start()