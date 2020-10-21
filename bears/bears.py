from datetime import date

class Bears:

    def __init__(self, name, species, walking, date_added, food):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date_added
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    # specifies what an object representation should be(this case a string)
    def __str__(self):
        return f"{self.name} is a {self.species}"
