# a generator is efficient because its values never persist in memory
for i in range(32): # at no point do all the numbers exist in memory
    print (i)

# python will make a generator for us if we need one
even_g = ( i for i in range(10) if i%2==0 )
print(type(even_g))
# a generator can yield values
print( even_g.__next__() ) # 0
print( even_g.__next__() ) # 2
print( even_g.__next__() ) # 4
# we can iterate over a generator
for member in even_g:
    print(member, end=', ')
# at this point, the generator is exhausted - it can yield no firther values
# print( even_g.__next__() ) # fails

# we can declare our own custom generators
def tally(incr):
    '''keep a tally of the incremental score (endlessly)'''
    score=0
    while True: # careful
        yield score # the yield statement makes this function into a generator
        score += incr

game = tally(5)
print(type(game))
print(next(game)) # 0
print(next(game)) # 5
print(next(game)) # 10
print(game.__next__()) # 15
# if we need to free up resources we can close the generator
game.close() # this will end hte infinite loop
