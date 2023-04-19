# we can read in the profile output file to see the results
import pstats

def main():
    #read in the output file
    p = pstats.Stats('review2/weather_profile')
    # print the results
    p.print_stats()

if __name__ == '__main__':
    main()