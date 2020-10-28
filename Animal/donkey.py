from datetime import date
from .animal import Animal

class Donkey(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"    

    def feed(self):
      print(f'{self.name} was given headpats while they were feed {self.food} on {date.today().strftime("%m/%d/%Y")}')
