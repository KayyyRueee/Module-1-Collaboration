class vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    def get_info(self):
        return f"{self.vehicle_type}"
    
class Automobile(vehicle):
    def __init__(self, make, model, year, doors, roof):
        super().__init__("Car")
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.roof = roof
    def get_info(self):
        return f" {self.make}, {self.model}, {self.year}, {self.doors}, {self.roof}"
    
print("Vehicle Type: Car")
Make = input("Make: ")
Model = input("Model: ")
Year = input("Year: ")
Doors = input("Doors: ")
Roof = input("Roof: ")

vehicle_automobile = Automobile( Make, Model, Year, Doors, Roof)
print("Make: ", vehicle_automobile.make)
print("Model: ", vehicle_automobile.model)
print("Year: ", vehicle_automobile.year)
print("Doors: ", vehicle_automobile.doors)
print("Roof: ", vehicle_automobile.roof)

