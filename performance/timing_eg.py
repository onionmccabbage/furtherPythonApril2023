from time import time
from timeit import default_timer

# here is a reasonably complex function (not a particularly performant way to calculate Fibonacci)
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2)) # iteratively call the same function
    
if __name__ == '__main__':
    n = 32
    # measure time as an indicator of performance (take averages)
    for i in range(0, 12):
        start_a = time() # time will simply clock the time according to this machine
        start_b = default_timer() # default_timer will attempt to measure only stuff done by python
        r = fib(n)
        # print(r)
        end_a   = time()
        end_b   = default_timer()
        print(f'Fibonacci up to {n} is {r} took {end_a-start_a} seconds (or {end_b-start_b} seconds)') # includes everything the machine was doing


