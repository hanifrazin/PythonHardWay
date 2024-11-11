class Mobil:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 2023
        self.description = ""

    def set_details(self, year = 2002, description = ""):
        self.year = year
        self.description = description

    def get_name(self):
        return f"{self.manufacturer} {self.name}"

    def info(self):
        print(f"Car name : {self.get_name()}")
        print(f"Description: {self.description}")
        print(f"Year Released: {self.year}")
        print()

# positional argument
car1 = Mobil()
car1.name = "M3 GTR"
car1.manufacturer = "BMW"
car1.set_details(2001, "Best car in NFS Most Wanted")
car1.info()

# optional argument
car2 = Mobil()
car2.name = "RX-8"
car2.manufacturer = "Mazda"
car2.set_details(description = "Best car in NFS Underground 2")
car2.info()

# keyword argument
car3 = Mobil()
car3.name = "Le Mans Quattro"
car3.manufacturer = "Audi"
car3.set_details(description="Best car in NFS Carbon", year=2003)
car3.info()