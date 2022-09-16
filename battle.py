import time
from collections import defaultdict


from classes import *


# Enemy is chosen from a list of enemies.
enemy = random.choice(enemyList)


def fight():

    print(str(mainHero.heroName) + " attacks " + str(enemy.enemyName) + "!")
    time.sleep(1.25)
    print(str(enemy.enemyName) + " lost " + str(mainHero.heroDMG) + "HP!")
    enemy.enemyHP -= mainHero.heroDMG
    time.sleep(1.25)

    if enemy.enemyHP > 0:
        print((str(enemy.enemyName) + " has " + str(enemy.enemyHP) + "HP left!\n"))
        time.sleep(1.25)

    elif enemy.enemyHP <= 0:
        time.sleep(0.75)
        print(str(enemy.enemyName) + " was defeadet!")
        time.sleep(1.25)

    if enemy.enemyHP > 0:
        print(str(enemy.enemyName) + " attacks " + str(mainHero.heroName) + "!")
        time.sleep(1.25)
        print(str(mainHero.heroName) + " lost " + str(enemy.enemyDMG) + "HP!")
        mainHero.heroHP -= enemy.enemyDMG
        time.sleep(1.25)

        if mainHero.heroHP > 0:
            print((str(mainHero.heroName) + " has " + str(mainHero.heroHP) + "HP left!\n"))
            time.sleep(1.25)

        elif mainHero.heroHP <= 0:
            time.sleep(0.75)
            print(str(mainHero.heroName) + " died", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\nGAME OVER")
            exit()


def battle():

    print("")
    print(str(enemy.enemyName) + " appears!")
    time.sleep(1)
    print(str(enemy.enemyName) + " has " + str(enemy.enemyHP) + "HP!\n")
    time.sleep(1)

    # Battle ends when the enemy loses all HP.
    while enemy.enemyHP > 0:
        print("What will " + str(mainHero.heroName) + " do?\n")

        # Battle menu system.
        print("1. Fight\n2. Items\n3. Escape")

        battle_option = int(input("\nOption: "))
        print("")

        # User clicks 1 for fight.
        if battle_option == 1:
            fight()

        # User clicks 2 to see inventory items.
        # TODO fix "x2" style indicator for duplicate items
        elif battle_option == 2:

            print(get_amount(inventory), "items in inventory\n")
            for item, count in itemAmount.items():
                print(f"x{count} {item}")

            #for i in inventory:
                    #print(i)

            print("\n1. Back to battle menu")
            print("2. Select item")

            battle_option = int(input("\nOption: "))
            print("")

        # User clicks 3 to escape the battle.
        elif battle_option == 3:
            print("filler")
