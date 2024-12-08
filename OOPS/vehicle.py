class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def Get_info(self):
        print("Make=",self.make,"Model of the vehicle=",self.model,"Year of the vehicle=",self.year)
    def start(self):
        print("The vehicle is starting")
class Car(Vehicle):
    def __init__(self, doors, fuel_type):
        self.doors=doors
        self.fuel_type=fuel_type
    def Get_info(self,Vehicle):
        


