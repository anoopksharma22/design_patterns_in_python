## Liskov Substitution Principle
It states that: If a program is using a base class, then derived classes must be substitutable without altering the correctness of the program

### Example:
Let consider the Order class example again we discussed in open-closed principle.
- Now the PaymentMethod clasess have new argument `security code`
- But PayPal doesn't uses `security code` is uses `email address`
- So our code works but we are abusing the `security code` parameter to use as email address and this violates the Liskow Substitution Principle.

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

class PaymentProcesor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PayByDebit(PaymentProcesor):

    def pay(self, order, security_code):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating Security code {security_code}")
        print(f"Paying by debit for order: {order.order_number}, total amount: {total_amount}")
  
class PayByCredit(PaymentProcesor):

    def pay(self, order, security_code):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating Security code {security_code}")
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")
  
class PayByPayPal(PaymentProcesor):

    def pay(self, order, security_code):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating email {security_code}")
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")
  

if __name__ == "__main__":
    item1 = Item("watch", 1, 5000)
    item2 = Item("phone", 2, 15000)
    item3 = Item("headphone", 5, 500)

    order1 = Order([item1, item2, item3])
    order2 = Order([item1, item3])

    pmc = PayByCredit()
    pmc.pay(order1,12324)
    
    pmd = PayByDebit()
    pmd.pay(order2,12334)

    pmpaypal = PayByDebit()
    pmpaypal.pay(order2,"email@email.com")
```

### Solution
This issue can be solved in a multiple ways, we just need to make sure the code works with any subclass of the baseclass on which the code depends.
- Subtypes must be substitutable for their base types.
- A subclass should not violate the expectations set by the base class.

Here we removed the `security code` from the pay method argument so that `pay` method is same accross all the sub classes \
Now the security code or email address is part of initializer of the sub class

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

class PaymentProcesor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PayByDebit(PaymentProcesor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating Security code {self.security_code}")
        print(f"Paying by debit for order: {order.order_number}, total amount: {total_amount}")
  
class PayByCredit(PaymentProcesor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating Security code {self.security_code}")
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")
  
class PayByPayPal(PaymentProcesor):

    def __init__(self, email):
        self.email = email

    def pay(self, order):
        total_amount = 0
        for item in order.items:
            total_amount += item.quantity * item.price
        print(f"Validating email {self.email}")
        print(f"Paying by credit for order: {order.order_number}, total amount: {total_amount}")
  

if __name__ == "__main__":
    item1 = Item("watch", 1, 5000)
    item2 = Item("phone", 2, 15000)
    item3 = Item("headphone", 5, 500)

    order1 = Order([item1, item2, item3])
    order2 = Order([item1, item3])

    pmc = PayByCredit(123)
    pmc.pay(order1)
    
    pmd = PayByDebit(222)
    pmd.pay(order2)

    pmpaypal = PayByDebit("email@email.com")
    pmpaypal.pay(order2)
```

### Another example:

In this example, `Penguin` inherits from `Bird` but overrides the `fly` method in a way that violates the expected behavior of the `Bird` class. This breaks the `Liskov Substitution Principle`, as you cannot substitute `Penguin` where a `Bird` is expected.

```python
class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly!")

def make_bird_fly(bird: Bird):
    print(bird.fly())

# Testing
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Works fine
make_bird_fly(penguin)  # Raises an exception

```

### Solution
```python
class Bird:
    def sound(self):
        return "Some generic bird sound"

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class NonFlyingBird(Bird):
    def fly(self):
        return "I cannot fly!"

class Sparrow(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    pass

def make_bird_fly(bird: Bird):
    if isinstance(bird, FlyingBird):
        print(bird.fly())
    else:
        print("This bird cannot fly.")

# Testing
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: I can fly!
make_bird_fly(penguin)  # Output: This bird cannot fly.
```

### Explanation
#### Refactored Hierarchy:
Bird represents the general concept of birds.\
FlyingBird and NonFlyingBird provide specific behaviors for flying and non-flying birds.\
#### Substitution:
Now, substituting Sparrow or Penguin for Bird won't break the program, as the correct behavior is enforced by the design.\
This adheres to the Liskov Substitution Principle while ensuring code correctness and clarity.