from datetime import date
from .animal import Animal

class Zebra(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        self.walking = True
        self.shift = shift
