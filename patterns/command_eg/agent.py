class Agent():
    '''the agent can issue commands
       Commands tend to be "doing" words '''
    def __init__(self):
        '''__orderQueue should only be accessible within this class'''
        self.__orderQueue = [] # start with an empty list
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        # the queue will let us wait for resources to become available 
        # before the command can be executed
        order.execute()

if __name__ == '__main__':
    pass