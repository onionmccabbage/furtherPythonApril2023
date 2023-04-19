import multiprocessing
import os # this gives access to the operating system
import time

def whoami():
    print(f'I am the process: {os.getpid()}')
    # see Get-Process | Select-String -Pattern "python" in powershell
    # or ps -eaf | grep python for linux
    time.sleep(5)

def main():
    procs = []
    # what is a sensible quantity of additional processes?
    # for n in range(os.cpu_count()): # NB you could also try GPU via CUDA
    for n in range(0, 9999):
        '''here we start new processes on their own process ID'''
        p = multiprocessing.Process(target=whoami)
        procs.append(p)
        p.start()
    # for p in procs:
    #     p.join()

if __name__ == '__main__':
    whoami()
    main()