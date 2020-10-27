from datetime import date
from .animal import Animal

class Tiger(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        
    def feed(self):
      print(f'{self.name} was fed carol baskin\'s {self.food} on {date.today().strftime("%m/%d/%Y")}')
