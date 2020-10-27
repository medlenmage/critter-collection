from .animal import Animal
from datetime import date

class Bears(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True

    # specifies what an object representation should be(this case a string)
    def __str__(self):
        return f"{self.name} is a {self.species}"
