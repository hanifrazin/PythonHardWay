from dataclasses import dataclass

@dataclass
class Country:
    name: str
    season: list
    number_of_population: float

    def info(self) -> str:
        return f"{self.name} | {len(self.season)} seasons | {self.number_of_population} million population"

countries = [
    Country("Indonesia",["Rainy","Dry"],275.5),
    Country("Palestine",["Winter","Summer","Autumn","Spring"], 5.044),
    Country("Mongolia",["Winter","Summer","Autumn","Spring"], 3.398)
]

for c in countries:
    print(c.info())