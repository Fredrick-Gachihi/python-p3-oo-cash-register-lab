#!/usr/bin/env python3
from cash_register import CashRegister

class TestCashRegister:
    def test_apply_discount(self):
        cash_register = CashRegister()
        cash_register_with_discount = CashRegister()  
        cash_register_with_discount.apply_discount(20)
        assert cash_register_with_discount.total == cash_register.tota

    def add_item(self, item, price, quantity=1):
        self.items.append({'item': item, 'price': price, 'quantity': quantity})
        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    def apply_discount(self, discount):
        discount_amount = (discount / 100) * self.total
        self.total -= discount_amount
        return self.total

    def void_last_transaction(self):
        if self.items:
            last_transaction = self.items.pop()
            self.total -= last_transaction['price'] * last_transaction['quantity']
            self.last_transaction_amount = 0
        else:
            print("No transactions to void.")

if __name__ == "__main__":
    register = CashRegister()
    register.add_item('Apple', 1.50, 2)
    register.add_item('Banana', 0.75)
    print("Total before discount:", register.total)
    register.apply_discount(10)
    print("Total after 10% discount:", register.total)
    register.void_last_transaction()
    print("Total after voiding last transaction:", register.total)