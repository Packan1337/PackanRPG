# Module for battles
from .fight import fight

def battle(enemy, hp):

    battle_option = 0

    print(enemy + " appears!")
    print(enemy + " has " + hp)
    print("What would you like to do?/n")

    print("1. Fight")
    print("2. Items")
    print("3. Escape")

    battle_option = int(input("Option: "))

    if battle_option == 1:

        fight()

