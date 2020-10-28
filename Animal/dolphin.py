from datetime import date
from .animal import Animal

class Dolphin(Animal):

    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was flung some {self.food} on {date.today().strftime("%m/%d/%Y")}')
