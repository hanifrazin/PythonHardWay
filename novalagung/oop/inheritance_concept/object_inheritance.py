class Vehicle:
    note = "class to represent a car"

    def __init__(self):
        self.name = "common vechicle"
        self.number_of_wheels = 4

    def drive_sound(self):
        return "vroom vroooommmm"

class ElectricCar(Vehicle):
    def info(self):
        print(f"{self.name} has {self.number_of_wheels} wheels. engine sound: {self.drive_sound()}")

v1 = Vehicle()
ket1 = "class inherit from class"
if isinstance(v1, Vehicle):
    print(f"v1 {ket1} {Vehicle.__name__}")
if isinstance(v1, object):
    print(f"v1 {ket1} object")

v2 = ElectricCar()
if isinstance(v2, ElectricCar):
    print(f"v2 {ket1} {ElectricCar.__name__}")
if isinstance(v2, Vehicle):
    print(f"v2 {ket1} {Vehicle.__name__}")
if isinstance(v2, object):
    print(f"v2 {ket1} object")