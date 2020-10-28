# from Animal import Bears, Chicken, Dolphin, Donkey, Elephant, Fish, Gorilla, Horse, Monkey, Sheep, Snake, Tiger, Whale, Wolf, Zebra
from Animal import Tiger
from attractions import PettingZoo, snakePit, wetlands


def main():

    castle_pets = PettingZoo("Castle Pets", "fuzzy little critters to pet")
    # shrek_swamp = wetlands("Shrek's Swamp", "this is my swamp")
    # sneaky_snakies = snakePit("Sneaky Snakes", "bring a recorder and they'll dance for you")

    # donkey = Donkey("Donkey", "donkey", "morning", "grass", 123)
    # slithers = Snake("Slithers", "python", "mice", 456)
    # nemo = Fish("Nemo", "clown fish", "pellets", 789)
    carol = Tiger("Carol", "Bengal", "husband\'s", 741)

    # castle_pets.animals.append(carol)
    # sneaky_snakies.animals.append(slithers)
    # shrek_swamp.animals.append(nemo)

    castle_pets.add_animal_pythonic(carol)

    carol.run()
    carol.swim()

    # print(donkey)

main()
