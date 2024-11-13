from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    diameter: float
    natural_sattelites: list[str]

planets = [
    Planet("Mercury",4879, []),
    Planet(name = "Venus", diameter = 12104, natural_sattelites = []),
    Planet(diameter = 12742, name = "Earth", natural_sattelites = ["Moon"]),
]

for p in planets:
    print(f"{p.name} | {p.diameter} km | {len(p.natural_sattelites)} moons")

mars = Planet("Mars", 4, ["Phobos","Deimos"])
mars.name = "Red Planet"
mars.diameter = 6779

print(f"{mars.name} | {mars.diameter} km | {len(mars.natural_sattelites)} moons")