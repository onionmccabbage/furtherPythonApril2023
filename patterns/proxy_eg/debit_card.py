from payment import Payment
from bank import Bank

# the debit card is a proxy for the bank
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input('swipe, tap or insert card? ')
        self.bank.setCard(card)
        return self.bank.do_pay() # True or False