from classes import *


def fight():

    # This was coded before I knew what f-strings were.
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
        obtain_item()
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
    mainHero.heroHP = maxHP

    global battle_option

    # Enemy is chosen from a list of enemies.
    global enemy
    enemy = random.choice(enemyList)

    # Reset enemy's HP from previous battle
    if enemy.enemyName == "Bazaar Turk":
        enemy.enemyHP = bt_max_hp

    elif enemy.enemyName == "Fat Ass Swamp Monster":
        enemy.enemyHP = fasm_max_hp

    elif enemy.enemyName == "Hairy Arab":
        enemy.enemyHP = ha_max_hp

    elif enemy.enemyName == "Huge Fucking Lizard":
        enemy.enemyHP = hfl_max_hp

    elif enemy.enemyName == "Keyboard Warrior":
        enemy.enemyHP = kw_max_hp

    print("")
    print(str(enemy.enemyName) + " appears!")
    time.sleep(1)
    print(str(enemy.enemyName) + " has " + str(round(enemy.enemyHP)) + "HP!\n")
    time.sleep(1)

    # Battle ends when the enemy loses all HP.
    while enemy.enemyHP > 0:
        print("What will " + str(mainHero.heroName) + " do?\n")
        time.sleep(1)

        while True:
            try:
                # Battle menu system.
                print("1. Fight\n2. Items\n3. Escape")

                battle_option = int(input("\nOption: "))
                print("")

                if isinstance(battle_option, int) \
                        and battle_option == 1 \
                        or battle_option == 2 \
                        or battle_option == 3:
                    break

                print("(Select by using a valid number!)\n")
                time.sleep(1.25)
            except ValueError:
                print("\n(Select by using a valid number!)\n")
                time.sleep(1.25)

        # User clicks 1 for fight.
        if battle_option == 1:
            fight()

        # User clicks 2 to see inventory items.
        elif battle_option == 2:
            display_items()

            while True:
                while True:
                    try:
                        print("\n1. Back to battle menu")

                        if allLargePotions or allNormalPotions or allDamageBuffers or allFireFlasks:
                            print("2. Select item")

                        battle_option = int(input("\nOption: "))
                        print("")

                        if battle_option == 1 or battle_option == 2:
                            break

                        if battle_option != 1 and battle_option != 2:
                            print("(Select by using a valid number!)\n")
                            time.sleep(1.25)

                    except ValueError:
                        print("\n(Select by using a valid number!)\n")
                        time.sleep(1.25)

                if battle_option == 2:

                    while True:
                        item_select_input = input("Type item to use: ")
                        item_select = item_select_input
                        time.sleep(0.5)

                        if item_select == "Potion":
                            use_item(normalPotion, enemy)
                            break

                        if item_select == "Large Potion":
                            use_item(largePotion, enemy)
                            break

                        if item_select == "Fire Flask":
                            use_item(fireFlask, enemy)
                            break

                        if item_select == "Damage Buffer":
                            use_item(damageBuffer, enemy)
                            break

                        if item_select != "Potion" or "Large Potion" or "Fire Flask" or "Damage Buffer":
                            print("\n(Type out the name of the item you want to use!)")
                            time.sleep(1.25)

                if battle_option == 1:
                    break

                break
        # User clicks 3 to escape the battle.
        elif battle_option == 3:
            print("Escaped from battle")
            time.sleep(1.25)
            break

    # After battle, hero obtains a new item.
    mainHero.heroDMG = reset_dmg
