class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

data1 = Car()
if isinstance(data1, Car):
    print(f"data1 class inherit from Car\n")
if isinstance(data1, object):
    print(f"data1 class inherit from object\n")

data2 = Car()
if isinstance(data2, Car):
    print(f"data2 class inherit from Car\n")
if isinstance(data2, object):
    print(f"data2 class inherit from object\n")