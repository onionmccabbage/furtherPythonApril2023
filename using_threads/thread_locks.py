import threading

# here is a global asset
counter = 0

def workerA():
    '''this function will access the global counter'''
    global counter
    try:
        while counter < 20:
            counter += 1
            print(f'worker A increments the counter to {counter}')
    except Exception as e:
        print(e)

def workerB():
    '''this function will access the global counter'''
    global counter
    try:
        while counter > -20:
            counter -= 1
            print(f'worker B decrements the counter to {counter}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()

    t1.join()
    t2.join()