from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta): # we inherit from ABC
    @abstractmethod
    def execute(self):
        pass # never implement in abstract


if __name__ == '__main__':
    pass