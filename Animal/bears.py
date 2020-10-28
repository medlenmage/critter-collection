from animal import Animal
from datetime import date
from movements import Swimming, Walking

class Bears(Animal, Swimming, Walking):

    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Swimming.__init__(self)
        Walking.__init__(self)

    # specifies what an object representation should be(this case a string)
    def __str__(self):
        return f"{self.name} is a {self.species}"
