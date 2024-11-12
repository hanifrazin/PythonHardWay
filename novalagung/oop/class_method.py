class ClanHouse:
    def __init__(self, name = "", house = ""):
        self.name = name
        self.house = house

    @classmethod
    def create(cls):
        obj = cls()
        return obj

    def info(self):
        print(f"{self.name} of {self.house}")

p1 = ClanHouse()
p1.name = "Paul"
p1.house = "Pamulang"
p1.info()

p2 = ClanHouse("Hopkin","Cibinong")
p2.info()

p3 = ClanHouse.create()
p3.name = "Brandon"
p3.house = "Bogor"
p3.info()