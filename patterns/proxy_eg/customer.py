from debit_card import DebitCard

class Customer(): # this is the client of the proxy
    def __init__(self):
        print('lets buy some stuff')
        self.debitCard = DebitCard() # an instance of our proxy
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay() # use our proxy
    def __del__(self):
        if self.isPurchased:
            print('we bought something')
        else:
            print('lend me a fiver?')
