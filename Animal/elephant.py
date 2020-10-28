from datetime import date
from .animal import Animal

class Elephant(Animal):

    def __init__(self, name, species, walking, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.walking = True

    def __str__(self):
        return f"{self.name} is a {self.species}"
