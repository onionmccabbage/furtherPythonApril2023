# decorators add something to what we already have

def showArgs(f): # NB 'f' is the function being decorated
    '''this will be a decorator for other functions
       Reveal all the positional arguments 
       and all the keyword arguments 
       passed in to any other function'''
    def newFunc(*args, **kwargs):
        # args is the tuple of any positional arguments
        # kwargs is the dictionary of any keyword arguments
        print(f'Running a function called {f.__name__}')
        print(f'Positional arguments are {args}')
        print(f'Keyword arguments are {kwargs}')
        # we need to run the function being decorated
        return f(*args, **kwargs)
    return newFunc

def otherDec(f):
    return f

# a few small functions
@showArgs # here we implement our decorator. It adds functionality to any other function
def addIntegers(a, b):
    return int(a) + int(b)

# careful - while decorators can be 'stacked' they will run the function immediately following, which might be another decorator
@showArgs
@otherDec
def raiseToPower(m, n):
    return m**n

if __name__ == '__main__':
    print( addIntegers(1, 2) )       # two positional arguments
    print( addIntegers(a=1, b=2) )   # two keyword arguments
    print( addIntegers(1, b=2) )     # a positional and a keyword argument
    print( raiseToPower(10, n=3) )