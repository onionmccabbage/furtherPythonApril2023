# modern python lets us manage asynchronous code using 'async'
# there was a feature for 'coroutines' largely subsumed by 'async'
import asyncio
import time

# decorate the function so it behaves as a coroutine
# Python will manage any threading and synchronicity
@asyncio.coroutine
def cube(n):
    '''this needs to be asynchronous (maybe it takes a long time)'''
    return n*n*n

# since asyncio is deprecated, we now have a new way to do it
# no need to import anything, no need to decorate anything, just use the 'async' keyword
async def square(n): # async makes this a coroutine (by managing threads)
    '''this function might take a while, so async means it will not block while awaiting'''
    await asyncio.sleep(2) # we would await calls to files, db, API ...
    return n*n

if __name__ == '__main__':
    # by calling a coroutine we are not blocking the flow of code
    s = asyncio.run( cube(3) )
    d = asyncio.run( square(2) )
    print(d)
    print(s)