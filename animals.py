from Animal import Bears, Chicken, Dolphin, Donkey, Elephant, Fish, Gorilla, Horse, Monkey, Sheep, Snake, Tiger, Whale, Wolf, Zebra
from attractions import PettingZoo, snakePit, wetlands


def main():

    castle_pets = PettingZoo("Castle Pets")
    shrek_swamp = wetlands("Shrek's Swamp")
    sneaky_snakies = snakePit("Sneaky Snakes")

    donkey = Donkey("Donkey", "donkey", "morning", "grass", 123)
    slithers = Snake("Slithers", "python", "mice", 456)
    nemo = Fish("Nemo", "clown fish", "pellets", 789)
    carol = Tiger("Carol", "Bengal", "husband's", 741)

    castle_pets.animals.append(donkey)
    sneaky_snakies.animals.append(slithers)
    shrek_swamp.animals.append(nemo)

    carol.run()
    carol.swim()

    print(donkey)

main()
