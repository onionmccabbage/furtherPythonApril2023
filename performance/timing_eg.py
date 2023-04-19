# there is a tool called cProfile - a performant way to profile non-trivial code
# invoke cProfile like this:
# python -m cProfile -o profiling_output timing_eg.py
# cProfile will record:
# number of calls, total time, time per call, cumulative time
# then write code to read in the generated profiling report


from time import time
from timeit import default_timer
from functools import reduce

# here is a reasonably complex function (not a particularly performant way to calculate Fibonacci)
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2)) # iteratively call the same function

def fib2(n):
    '''This method is way more performant'''
    sequence = (0,1)
    for _ in range(2, n+1):
        '''repeatedly add the last two values of the sequence'''
        sequence += (reduce(lambda a,b: a+b, sequence[-2:]), ) # careful - must be a tuple
    return sequence[n]

if __name__ == '__main__':
    # n = 38 # ~7 seconds for Fib
    n=10000 # ~0.3 sec for Fib2
    # measure time as an indicator of performance (take averages)
    for i in range(0, 12):
        start_a = time() # time will simply clock the time according to this machine
        start_b = default_timer() # default_timer will attempt to measure only stuff done by python
        r = fib2(n)
        # print(r)
        end_a   = time()
        end_b   = default_timer()
        print(f'Fibonacci up to {n} is {r} took {end_a-start_a} seconds (or {end_b-start_b} seconds)') # includes everything the machine was doing


