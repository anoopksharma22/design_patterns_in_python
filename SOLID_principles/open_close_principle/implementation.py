from abc import ABC, abstractmethod

class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Order:
    counter = 0
    def __init__(self, items):
        self.order_number = self.generate_order_number()
        self.items = items

    @classmethod
    def generate_order_number(cls):
        cls.counter += 1
        print(f"Generating new order number {cls.counter}")
        return cls.counter

# class PaymentProcesor:
    
#     def pay_by_credit(self, order):
#         total_amount = 0
#         for item in order.items:
#             total_amount += item.quantity * item.price
        
#         print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")

#     def pay_by_debit(self, order):
#         total_amount = 0
#         for item in order.items:
#             total_amount += item.quantity * item.price
        
#         print(f"Paying by debit for order: {order.order_number}, total amount: {total_amount}")


class PaymentProcesor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PayByDebit(PaymentProcesor):

    def pay(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        
        print(f"Paying by debit for order: {order.order_number}, total amount: {total_amount}")
  
class PayByCredit(PaymentProcesor):

    def pay(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")
  

if __name__ == "__main__":
    item1 = Item("watch", 1, 5000)
    item2 = Item("phone", 2, 15000)
    item3 = Item("headphone", 5, 500)

    order1 = Order([item1, item2, item3])
    order2 = Order([item1, item3])

    pmc = PayByCredit()
    pmc.pay(order1)
    
    pmd = PayByDebit()
    pmd.pay(order2)