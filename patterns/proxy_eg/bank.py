from payment import Payment
import random # the bank will respond randomly

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print(f'Bank is checking if {self.__getAccount} has funds')
        # randomly decide...
        return bool(random.getrandbits(1)) # True or False
    def do_pay(self):
        if self.__hasFunds():
            print('bank is paying')
            return True
        else:
            print('insufficient funds')
            return False
