from datetime import date
from .animal import Animal

class Fish(Animal):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"
