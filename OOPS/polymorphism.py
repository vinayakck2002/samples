#polymorphism
#only 
class Vehicle:
    def move():
        print("its moving")
class Car(Vehicle):
    def move():
        print("Its not moving")
class Bike(Vehicle):
    def move():
        print("Its")
obj=Bike
obj.move()#output:-Its
