from datetime import date
from .animal import Animal

class Snake(Animal):
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
      print(f'{self.name} had {self.food} dangled to them on {date.today().strftime("%m/%d/%Y")}')
