from .animal import Animal
from datetime import date

class Chicken(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed(self):
      print(f'{self.name} was thrown some {self.food} on {date.today().strftime("%m/%d/%Y")}')
