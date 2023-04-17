

# a bunch of classes to achieve stuff
class Coder():
    '''creates code to solve problems'''
    def __init__(self):
        print('write some code')
    def __is_available__(self):
        print('coding skills are available') # we might check availability
        return True # or False
    def book_time(self):
        if self.__is_available__():
            print('coder has been booked')

class Tester():
    '''tests code to ensure diligence'''
    def __init__(self):
        print('preparing tests')
    def testing(self):
        print('tests are in place')

class Technician():
    '''solve technical issues'''
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines and stuff are in place')

class Artisan():
    '''design stuff'''
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

# a manager is the facade to all the other skills
class Manager():
    '''manage the other roles'''
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # the facade will provide instances of all the subsystems/microservices
        self.coder      = Coder()
        self.tester     = Tester()
        self.technician = Technician()
        self.artisan    = Artisan()
        # put them to work (we could pass in parameters)
        self.coder.book_time()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.make_prototype()

# here is a client - they need to get a project going
class Client():
    def __init__(self):
        print('we need a project team')
    def askManager(self):
        print('lets talk to the manager')
        self.m = Manager()
        self.m.arrange() # the facade (manager) deals with all the subsystems
    def __del__(self): # every class in Python will run its __del__ method when finished
        print('all done')


if __name__ == '__main__':
    '''a facade makes ugly stuff easier to look at'''
    customer = Client()
    customer.askManager() # get things going
