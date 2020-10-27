from datetime import date
from .animal import Animal
from movements import Swimming, Walking

class Tiger(Animal, Swimming, Walking):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        
    def feed(self):
      print(f'{self.name} was fed carol baskin\'s {self.food} on {date.today().strftime("%m/%d/%Y")}')
