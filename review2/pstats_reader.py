# we can read in the profile output file to see the results
import pstats

def main():
    #read in the output file
    p = pstats.Stats('out')
    # print the results
    p.print_stats()

if __name__ == '__main__':
    main()