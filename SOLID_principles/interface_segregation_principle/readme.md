## Interface Segregation Principle
A class should not be forced to implement interfaces it does not use.

In simpler terms:
- Instead of creating large, general-purpose interfaces, create smaller, more specific ones.
- This prevents implementing classes from being burdened with methods they don't need or use.

### Example
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving on the road"

    def fly(self):
        raise NotImplementedError("Cars cannot fly!")

class Airplane(Vehicle):
    def drive(self):
        raise NotImplementedError("Airplanes cannot drive!")

    def fly(self):
        return "Flying in the sky"

# Testing
car = Car()
airplane = Airplane()

print(car.drive())  # Works fine
print(car.fly())    # Raises NotImplementedError

```
### Issue:
In this example:
- The Vehicle interface enforces all classes to implement both drive and fly.
- This creates a problem because Car cannot fly, and Airplane cannot drive.

### Solution:

```python
from abc import ABC, abstractmethod

class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Car(Drivable):
    def drive(self):
        return "Driving on the road"

class Airplane(Drivable, Flyable):
    def drive(self):
        return "Taxiing on the runway"

    def fly(self):
        return "Flying in the sky"

# Testing
car = Car()
airplane = Airplane()

print(car.drive())      # Output: Driving on the road
print(airplane.drive()) # Output: Taxiing on the runway
print(airplane.fly())   # Output: Flying in the sky

```

### Explanation

- Drivable and Flyable are smaller, specific interfaces.
- Car only implements Drivable, avoiding unnecessary methods.
- Airplane implements both Drivable and Flyable.

#### Benefits:
- Classes only implement the interfaces relevant to them.
- Better separation of concerns and flexibility.

