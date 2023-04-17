# import from our other modules
from stock_trade import StockTrade
from agent import Agent
from buy_stock import BuyStock
from sell_stock import SellStock

def main():
    '''call the other package classes and issue commands'''
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke the commands
    agent.placeOrder(buy)
    agent.placeOrder(sell)

if __name__ == '__main__':
    main()