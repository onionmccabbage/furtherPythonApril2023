import threading

# here is a global asset
counter = 0
# we can provide a thread lock
lock = threading.Lock() # we have an isntance of a lock

def workerA():
    '''this function will access the global counter'''
    global counter
    lock.acquire() # this function has exclusive use of the lock
    try:
        while counter < 20:
            counter += 1
            print(f'worker A increments the counter to {counter}')
    except Exception as e:
        print(e)
    finally:
        lock.release()

def workerB():
    '''this function will access the global counter'''
    global counter
    lock.acquire() # this function has exclusive use of the lock
    try:
        while counter > -20:
            counter -= 1
            print(f'worker B decrements the counter to {counter}')
    except Exception as e:
        print(e)
    finally:
        lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()

    t1.join()
    t2.join()