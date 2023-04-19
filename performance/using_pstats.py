# pstats is capable of reading the output from cProfile
import pstats

def main():
    '''read in the profiling output from cProfile and print it'''
    # be careful with the path to the file - depends where you run Python from
    p = pstats.Stats('performance/profiling_output')
    p.print_stats()

if __name__ == '__main__':
    main()