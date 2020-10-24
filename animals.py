from bears import Bears
from chicken import Chicken
from dolphin import Dolphin
from donkey import Donkey
from elephant import Elephant
from fish import Fish
from gorilla import Gorilla
from horse import Horse
from monkey import Monkey
from sheep import Sheep
from snake import Snake
from tiger import Tiger
from whale import Whale
from wolf import Wolf
from zebra import Zebra
from pettingZoo import PettingZoo
from snakePit import snakePit
from wetlands import wetlands


def main():

    castle_pets = PettingZoo("Castle Pets")
    shrek_swamp = wetlands("Shrek's Swamp")
    sneaky_snakies = snakePit("Sneaky Snakes")

    donkey = Donkey("Donkey", "donkey", "morning", "grass")
    slithers = Snake("Slithers", "python", "mice")
    nemo = Fish("Nemo", "clown fish", "pellets")


    castle_pets.animals.append(donkey)
    sneaky_snakies.animals.append(slithers)
    shrek_swamp.animals.append(nemo)

    print(donkey)

main()
