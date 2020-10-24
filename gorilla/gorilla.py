from datetime import date

class Gorilla:

    def __init__(self, name, species, walking, food, chip_num):
        self.name = name
        self.species = species
        self.walking = walking
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
