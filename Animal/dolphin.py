from datetime import date
from .animal import Animal

class Dolphin(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
      print(f'{self.name} was flung some {self.food} on {date.today().strftime("%m/%d/%Y")}')
