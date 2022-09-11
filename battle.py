# Module for battles
import fight
from classes import Enemy
from classes import Hero
def battle():

    battle_option = 0

    print(Enemy.enemyName + " appears!")
    print(Enemy.enemyName + " has " + Enemy.enemyHP)
    print("What would you like to do?/n")

    print("1. Fight")
    print("2. Items")
    print("3. Escape")

    battle_option = int(input("Option: "))

    if battle_option == 1:

        fight()

