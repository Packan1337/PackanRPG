# Module for battles
import fight, random
from classes import Enemy
from classes import enemyList, items

def battle():

    battle_option = 0

    enemy = random.choice(enemyList)
    
    print(str(enemy.enemyName) + " appears!")
    print(str(enemy.enemyName) + " has " + str(enemy.enemyHP) + "HP!\n")
    print("What would you like to do?\n")

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


battle()
