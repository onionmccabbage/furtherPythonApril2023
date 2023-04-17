from order import Order

class BuyStock(Order):
    def __init__(self,stock):
        self.stock =stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if new_stock != '':
            self.__stock= new_stock
        else:
            raise Exception('problem with stock')
    def execute(self):
        '''only works when we have actual stock to sell'''
        return self.stock.buy()


if __name__ == '__main__':
    b = BuyStock('Athlone')
    print(f'bought {b.stock}')
