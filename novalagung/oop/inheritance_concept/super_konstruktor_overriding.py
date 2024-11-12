class Vehicle:
    note = "class to represent a car"

    def __init__(self):
        self.name = "common vechicle"
        self.number_of_wheels = 4

    def drive_sound(self):
        return "vroom vroooommmm"

class ElectricCar(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "electric car"

    def info(self):
        print(f"{self.name} has {self.number_of_wheels} wheels. engine sound: {self.drive_sound()}")

v1 = Vehicle()
print(f"{v1.name} has {v1.number_of_wheels} wheels. engine sound: {v1.drive_sound()}")

v2 = ElectricCar()
print(f"{v2.name} has {v2.number_of_wheels} wheels. engine sound: {v2.drive_sound()}")

v3 = ElectricCar()
v3.info()