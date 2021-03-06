from datetime import date
from .animal import Animal

class Whale(Animal):

    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"
