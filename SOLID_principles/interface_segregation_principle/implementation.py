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
