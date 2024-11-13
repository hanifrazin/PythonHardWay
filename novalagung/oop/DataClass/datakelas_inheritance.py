from dataclasses import dataclass


@dataclass
class Animal:
    name: str

    def info(self):
        return self.name

@dataclass
class Bird(Animal):
    super()
    can_fly: bool

    def info(self):
        super().info()
        return f"{self.name} can fly? {self.can_fly}"

cow = Animal(name = "Cow")
print(cow.info())

chicken = Bird(name = "Chicken",can_fly = False)
print(chicken.info())
