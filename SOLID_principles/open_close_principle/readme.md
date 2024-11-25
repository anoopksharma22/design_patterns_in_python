## Open-Closed Principle
The systems should be open to extensions but closed to modifications. It means once base classes are defined they should not be modified rather they should be extended to add more functionalities.

Programing concepts used to implement open close principle:

    Inheritance
    Interfaces
    Polymorphism

### Example:
We have an order class, a order can have list of items and we can pay using PaymentProcessor class.

```python

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

class PaymentProcesor:
    
    def pay_by_credit(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")

    def pay_by_debit(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        
        print(f"Paying by debit for order: {order.order_number}, total amount: {total_amount}")



if __name__ == "__main__":
    item1 = Item("watch", 1, 5000)
    item2 = Item("phone", 2, 15000)
    item3 = Item("headphone", 5, 500)

    order1 = Order([item1, item2, item3])
    order2 = Order([item1, item3])

    pp = PaymentProcesor()
    pp.pay_by_credit(order1)
    pp.pay_by_debit(order2)

```

### Issue with this design
- If we want to add another payment method then we need to modify the PaymentProcessor class which violates the Open-Closed principle.
- This is an issue because the code is already in production and if we modify it we need to test all the feature which depends on it.

### Solution
We can create an abstract class PaymentProcessor class and create sub classes for ecah payment methods or types.

```python
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
```