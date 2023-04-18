# semaphores let us specify the maximum number of concurrent threads accessing a resource
# here we have 'tickets' to be sold. ticket sellers will run on separate threads

import random
import time
import threading

# a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''use s semaphore to access the tickets to be sold'''
    ticketsSold = 0
    def __init__(self, sem): # pass in a semaphore
        threading.Thread.__init__(self)
        self.__sem = sem
    def run(self):
        global ticketsAvailable
        running = True
        while running:
            self.__sem.acquire() # like locks and rlocks, but with multiple concurrent acess
            self.randomDelay()
            if ticketsAvailable <=0:
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
            self.__sem.release()
            time.sleep(0.01) # delay the thread
        print(f'Ticket seller {self.getName()} sold {self.ticketsSold} tickets')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5 or 0.75 seconds

def main():
    '''provide a semaphore then a bunch of tixket seller instances'''
    sem = threading.Semaphore()
    sellers = []
    for i in range(0,4):
        seller = TicketSeller(sem) # all the threads share the one semaphore
        sellers.append(seller)
        seller.start()
    # once all the threads have started, we can join them
    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    main()