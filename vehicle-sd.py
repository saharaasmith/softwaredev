# Sahara Smith
# filename: Vehicle-sd
# This app will accept user input for information about a car (year, make, model, door amount, and roof type) then outputs it to the user.
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, door_amount, roof_type):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.door_amount = door_amount
        self.roof_type = roof_type

# Input Data
vehicle_type = "Car"
year = int(input("Input Year: "))
make = input("Input Make: ")
model = input("Input Model: ")
while True:
    try:
        door_amount = int(input("Input Door Amount (2 or 4): "))
        if door_amount == 2 or door_amount == 4:
            break
        else:
            print("Invalid. Please Input 2 or 4")
    except ValueError:
        print("Invalid. Please Input 2 or 4")
while True:
    try:
        roof_type = input("Input Roof Type (Solid or Sun-Roof): ").lower()
        if roof_type == "Solid" or roof_type == "Sun-Roof":
            break
        else:
            print("Invalid. Please enter 'Solid' or 'Sun-Roof'")
    except ValueError:
        print("Invalid. Please enter 'Solid' or 'Sun-Roof'")
car_info = Automobile(vehicle_type, year, make, model, door_amount, roof_type)

# Output Data
print("Vehicle Type:", vehicle_type)
print("Year:", car_info.year)
print("Make:", car_info.make)
print("Model:", car_info.model)
print("Number of Doors:", car_info.door_amount)
print("Roof Type:", car_info.roof_type)
