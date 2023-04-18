# we can enumerate the running threads
import time
import random
from threading import Thread
from threading import enumerate

def threadWorker(i):
    print(f'thread {i} has started')
    time.sleep(random.randint(1,2))
    print(f'thread {i} is terminating')

if __name__ == '__main__':
    myThread = Thread(target=threadWorker, args=('t1',))
    myThread.start()
    myThread.join()
    for i in range(0, 128):
        thread = Thread(target=threadWorker, args=(i, ))
        thread.start()
        print(f'Active threads: {enumerate()}')