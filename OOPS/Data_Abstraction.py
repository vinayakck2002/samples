from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass
class Car(Vehicle):
    def move():
        print("its not moving")
obj=Car
obj.move()#output:-Its not moving
