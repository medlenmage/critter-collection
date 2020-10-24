class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def get_animals(self):
        print(f"{self.attraction_name} is where the {self.description} are")
        for animal in self.animals:
            print(animal)

@property
def last_critter_added(self):
    return f'\t* {self.animals[-1].name} the {self.animals[-1].species}'
