import time

from classes import *


def fight():

    # Hero attacks enemy.
    print(str(mainHero.heroName) + " attacks " + str(enemy.enemyName) + "!")
    time.sleep(1.25)
    print(str(enemy.enemyName) + " lost " + str(round(mainHero.heroDMG)) + "HP!")
    enemy.enemyHP -= mainHero.heroDMG
    time.sleep(1.25)

    # Check if enemy is alive, then prints HP value.
    if enemy.enemyHP > 0:
        print((str(enemy.enemyName) + " has " + str(round(enemy.enemyHP)) + "HP left!\n"))
        time.sleep(1.25)

    # Check if enemy is dead, then prints victory message.
    elif enemy.enemyHP <= 0:
        time.sleep(0.75)
        print(str(enemy.enemyName) + " was defeadet!\n")
        time.sleep(1.25)

    # Enemy attacks hero.
    if enemy.enemyHP > 0:
        print(str(enemy.enemyName) + " attacks " + str(mainHero.heroName) + "!")
        time.sleep(1.25)
        print(str(mainHero.heroName) + " lost " + str(round(enemy.enemyDMG)) + "HP!")
        mainHero.heroHP -= enemy.enemyDMG
        time.sleep(1.25)

        # Checks if hero is alive, then prints HP value.
        if mainHero.heroHP > 0:
            print((str(mainHero.heroName) + " has " + str(round(mainHero.heroHP)) + "HP left!\n"))
            time.sleep(1.25)

        # Checks if hero is dead, then prints Game Over message.
        elif mainHero.heroHP <= 0:
            time.sleep(0.75)
            print("")
            print(str(mainHero.heroName) + " died", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\nGAME OVER")
            time.sleep(3)
            exit()


def battle():

    print("")
    print(str(enemy.enemyName) + " appears!")
    time.sleep(1)
    print(str(enemy.enemyName) + " has " + str(round(enemy.enemyHP)) + "HP!\n")
    time.sleep(1)

    # Battle ends when the enemy loses all HP.
    while enemy.enemyHP > 0:
        print("What will " + str(mainHero.heroName) + " do?\n")
        time.sleep(1)

        # Battle menu system.
        print("1. Fight\n2. Items\n3. Escape")

        battle_option = int(input("\nOption: "))
        print("")

        # User clicks 1 for fight.
        if battle_option == 1:
            fight()

        # User clicks 2 to see inventory items.
        elif battle_option == 2:
            display_items()

            print("\n1. Back to battle menu")
            print("2. Select item")

            item_select_state = int(input("\nOption: "))
            print("")

            if item_select_state == 2:

                item_select_input = input("Type item to use: ")
                item_select = item_select_input

                if item_select == "Potion":
                    use_item(normalPotion)

                if item_select == "Large Potion":
                    use_item(largePotion)

                if item_select == "Fire Flask":
                    use_item(fireFlask)

                if item_select == "Damage Buffer":
                    use_item(damageBuffer)

                if enemy.enemyHP > 0:
                    print(str(enemy.enemyName) + " attacks " + str(mainHero.heroName) + "!")
                    time.sleep(1.25)
                    print(str(mainHero.heroName) + " lost " + str(round(enemy.enemyDMG)) + "HP!")
                    mainHero.heroHP -= enemy.enemyDMG
                    time.sleep(1.25)

                    # Checks if hero is alive, then prints HP value.
                    if mainHero.heroHP > 0:
                        print((str(mainHero.heroName) + " has " + str(round(mainHero.heroHP)) + "HP left!\n"))
                        time.sleep(1.25)

                    # Checks if hero is dead, then prints Game Over message.
                    elif mainHero.heroHP <= 0:
                        time.sleep(0.75)
                        print("")
                        print(str(mainHero.heroName) + " died", end="")
                        time.sleep(1)
                        print(".", end="")
                        time.sleep(1)
                        print(".", end="")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\nGAME OVER")
                        time.sleep(3)
                        exit()

        # User clicks 3 to escape the battle.
        elif battle_option == 3:
            print("Escaped from battle")

    # After battle, hero obtains a new item.
    obtain_item()
    mainHero.heroDMG = reset_dmg
