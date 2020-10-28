from datetime import date
from .animal import Animal

class Snake(Animal):
    
    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} had {self.food} dangled to them on {date.today().strftime("%m/%d/%Y")}')
