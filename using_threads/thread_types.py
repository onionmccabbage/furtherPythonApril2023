# threads can run from functions or from classes
from threading import Thread # NB Thread is a thread-access object (not an actual thread)
import time
import random
import timeit # this is the most accurate way to measure code run time
from memory_profiler import profile

@profile # this will report on the function 
def someFn(name):
    '''this function wil simply sleep for a random time'''
    for i in range(0, 50):
        time.sleep(random.random()*0.1) # sleep for up to a tenth of a second
        print(name)

class SomeClass(Thread):
    def __init__(self, name):
        Thread.__init__(self) # call the initializer on the Thread class
        self.name = name
    @profile # this will report on the method of this class
    def run(self): # this can be called to run our thread
        for i in range(0,50):
            time.sleep(random.random()*0.1) # sleep for up to a tenth of a second
            print(self.name)

if __name__ == '__main__':
    # NB all these threads will run on ONE processor
    # we can make a function run on a new thread
    t1 = Thread(target=someFn, args=('thread 1',)) # NB the args MUST be a tuple
    t2 = Thread(target=someFn, args=('thread 2',)) # NB the args MUST be a tuple
    t3 = SomeClass('thread 3')
    t4 = SomeClass('thread 4')
    # threads run at the same time, so many threads can be concurrent
    start = timeit.default_timer()
    t1.start() # here we start the new thread
    t2.start() # here we start the new thread
    t3.start() # here we start the new thread (calls the run method of the class)
    t4.start() # here we start the new thread

    t1.join() # here we join the new thread back to the main thread
    t2.join() # here we join the new thread back to the main thread
    t3.join() # here we join the new thread back to the main thread
    t4.join() # here we join the new thread back to the main thread
    end = timeit.default_timer()
    print(f'All threads completed in {end-start}')