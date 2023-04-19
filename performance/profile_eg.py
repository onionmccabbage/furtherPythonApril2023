from memory_profiler import profile # may need to pip install memory_profiler
import collections # a bunch of additonal data structures

@profile # invoke the memory profiler
def someFn():
    '''manage a double-ended queue'''
    my_deq = collections.deque('98765432')
    print(f'Deque: {my_deq}')
    my_deq.append('1')
    print(f'Deque: {my_deq}')
    my_deq.appendleft('0')
    print(f'Deque: {my_deq}')
    my_deq.pop()
    print(f'Deque: {my_deq}')
    my_deq.popleft()
    print(f'Deque: {my_deq}')
    # we can make use of loads of memory
    for i in range(0, 1024**2): # a better solution would be a generator (doesnt persist values in memory)
        my_deq.append(str(i))

if __name__ == '__main__':
    someFn()
