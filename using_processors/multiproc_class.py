import multiprocessing
import os
import time

from memory_profiler import profile

class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    @profile
    def run(self):
        time.sleep(2)
        print(f'Child process ID is {multiprocessing.current_process().pid}')

def main():
    procs = []
    for n in range(os.cpu_count()): # NB you could also try GPU via CUDA
        '''here we start new processes on their own process ID'''
        p = MyProcess()
        procs.append(p)
        p.start()
    for p in procs:
        p.join()

if __name__ == '__main__':
    main()