from bank import Bank
from customer import Customer
from debit_card import DebitCard
from payment import Payment

def main():
    customer = Customer()
    customer.makePayment()

if __name__ == '__main__':
    main()