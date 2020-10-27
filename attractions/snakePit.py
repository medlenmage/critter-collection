from .attractions import Attraction

class snakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def get_animals(self):
        print(f"{self.attraction_name} is where the {self.description} are")
        for animal in self.animals:
            print(animal)

@property
def last_critter_added(self):
    return f'\t* {self.animals[-1].name} the {self.animals[-1].species}'
