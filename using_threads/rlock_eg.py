# rlock is a re-entrant lock

import threading
import time

class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2 # the threads may need to access these values
        self.rlock = threading.RLock() # re-entrant lock
    def modifyA(self):
        with self.rlock: # NBB using 'with' means we never need to release the lock (it will be released when no longer needed)
            print(f'RLock acquired: {self.rlock._is_owned()}, modifying A')
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        with self.rlock:
            print(f'RLock acquired: {self.rlock._is_owned()}, modifying B')
            self.b -= 1
            time.sleep(1)
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

if __name__ == '__main__':
    worker = MyWorker() # we are staying on the main thread
    worker.modifyA()
    worker.modifyB()
    worker.modifyBoth()