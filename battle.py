# Module for battles
import random
from classes import enemyList, items
from classes import mainHero


# Enemy is chosen from a list of enemies.
enemy = random.choice(enemyList)


def fight():

    print(mainHero.heroName + " attacks " + enemy.enemyName + "!")
    print(enemy.enemyName + " lost " + mainHero.heroDMG + "HP!")

    if enemy.enemyHP > 0:
        print(enemy.enemyName + " attacks " + mainHero.heroName + "!")
        print(mainHero.heroName + "lost" + enemy.enemyDMG + "HP!")


def battle():

    print("")
    print(str(enemy.enemyName) + " appears!")
    print(str(enemy.enemyName) + " has " + str(enemy.enemyHP) + "HP!\n")

    # Battle ends when the enemy loses all HP.
    while enemy.enemyHP > 0:
        print("What will " + mainHero + " do?\n")

        # Battle menu system.
        print("1. Fight")
        print("2. Items")
        print("3. Escape")

        battle_option = int(input("\nOption: "))
        print("")

        # User clicks 1 for fight.
        if battle_option == 1:
            fight()

        # User clicks 2 to see inventory items.
        elif battle_option == 2:
            print("Items in inventory\n")
            print(*items, sep="\n")

        # User clicks 3 to escape the battle.
        elif battle_option == 3:
            print("filler")
