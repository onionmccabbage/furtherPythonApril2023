from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass