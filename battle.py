# Module for battles
import fight
import random
from classes import enemyList, items
from main import heroNameMain


def battle():

    battle_option = 0

    enemy = random.choice(enemyList)

    print("")
    print(str(enemy.enemyName) + " appears!")
    print(str(enemy.enemyName) + " has " + str(enemy.enemyHP) + "HP!\n")

    while enemy.enemyHP > 0:
        print("What will " + heroNameMain + " do?\n")

        print("1. Fight")
        print("2. Items")
        print("3. Escape")

        battle_option = int(input("\nOption: "))
        print("")

        if battle_option == 1:

            fight()

        elif battle_option == 2:
            print("Items in inventory\n")
            print(*items, sep="\n")

        elif battle_option == 3:
            print(enemy)
