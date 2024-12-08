# Create a base class Vehicle:

# Attributes: make (string), model (string), year (integer)
# Methods:
# get_info() that returns the make, model, and year of the vehicle.
# start() that prints "The vehicle is starting."
# Create a subclass Car that inherits from Vehicle:

# Attributes: doors (integer), fuel_type (string)
# Method:
# get_info() that overrides the method in Vehicle and includes the number of doors and fuel type.
# honk() that prints "The car is honking!"
# Create another subclass Truck that inherits from Vehicle:

# Attributes: cargo_capacity (float), truck_type (string)
# Method:
# get_info() that overrides the method in Vehicle and includes the cargo capacity and truck type.
# load_cargo() that prints "Cargo is being loaded."
# Write a program to:

# Create objects for Car and Truck.
# Call the get_info() method for both objects.
# Call the honk() method for the Car object.
# Call the load_cargo() method for the Truck object.

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make        
        self.model=model
        self.year=year
    def get_info(self):
        print("Make=",self.make,"Model of the vehicle=",self.model,"Year of the vehicle=",self.year)    
    def start(self):
        print("The vehicle is starting")    
class Car(Vehicle):
    def __init__(self,make,model,year,doors,fuel_type):
        super().__init__(make,model,year)
        self.doors=doors
        self.fuel_type=fuel_type
    def get_info(self):
        super().get_info()
        print("Number of doors=",self.doors,"Fuel type=",self.fuel_type)
    def honk(self):
        print("The car is honking!")
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,truck_type):    
        super().__init__(make,model,year)
        self.cargo_capacity=cargo_capacity    
        self.truck_type=truck_type
    def get_info(self):
        super().get_info()
        print("Cargo capacity=",self.cargo_capacity,"Truck type=",self.truck_type)
    def load_cargo(self):
        print("Cargo is being loaded.")

