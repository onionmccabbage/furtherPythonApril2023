# a daemon thread will continue to run until the main thread terminates
from threading import Thread
import time
def standardThread():
    print('starting standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonThread():
    while True: # an endless loop - use with caution
        print('heartbeat.....')
        time.sleep(0.25)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread)
    d.setDaemon(True) # now that thread will run continuously
    s.start()
    d.start()
    s.join()
    d.join() # careful - the daemon will NEVER end, so you must terminate the main thread