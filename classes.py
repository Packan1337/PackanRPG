import random
import time


class Enemy:

    def __init__(self, enemy_name, enemy_hp, enemy_dmg):
        self.enemyName = str(enemy_name)
        self.enemyHP = float(enemy_hp)
        self.enemyDMG = float(enemy_dmg)

    def __str__(self):
        return self.enemyName


enemyList = [Enemy("Bazaar Turk", 23, 3),
             Enemy("Fat Ass Swamp Monster", 15, 5),
             Enemy("Hairy Arab", 17, 3),
             Enemy("Huge Fucking Lizard", 15, 5),
             Enemy("Keyboard Warrior", 22, 5)]

bt_max_hp = enemyList[0].enemyHP
fasm_max_hp = enemyList[1].enemyHP
ha_max_hp = enemyList[2].enemyHP
hfl_max_hp = enemyList[3].enemyHP
kw_max_hp = enemyList[4].enemyHP


class Hero:

    def __init__(self, hero_name):
        self.heroName = str(hero_name)
        self.heroHP = float(25)
        self.heroDMG = float(10)

    def __str__(self):
        return self.heroName


# Saves user's name
name = ""
mainHero = Hero(name)
maxHP = mainHero.heroHP
reset_dmg = mainHero.heroDMG


class Item:

    def __init__(self, item_name, item_heal, item_dmg, item_buff, item_desc):
        self.itemName = str(item_name)
        self.itemHeal = float(item_heal)
        self.itemDmg = float(item_dmg)
        self.itemBuff = float(item_buff)
        self.itemDesc = str(item_desc)


normalPotion = Item("Potion", 10, 0, 0, "Heals for 10HP.")
largePotion = Item("Large Potion", 20, 0, 0, "Heals for 20HP.")
fireFlask = Item("Fire Flask", 0, 20, 0, "Deals 20 damage.")
damageBuffer = Item("Damage Buffer", 0, 0, 1.5, "Increases damage by 50%.")

# Unique lists for each item.
allNormalPotions = []
allLargePotions = []
allFireFlasks = []
allDamageBuffers = []


# Functions that generate new item object.
def generate_normal_potion():
    print("Item reward: x1 Potion\n")
    potion = Item("Potion", 10, 0, 0, "Heals for 10HP.")
    allNormalPotions.append(potion)


def generate_large_potion():
    print("Item reward: x1 Large Potion\n")
    large_potion = Item("Large Potion", 20, 0, 0, "Heals for 20HP.")
    allLargePotions.append(large_potion)


def generate_fire_flask():
    print("Item reward: x1 Fire Flask\n")
    fire_flask = Item("Fire Flask", 0, 20, 0, "Deals 20 damage.")
    allFireFlasks.append(fire_flask)


def generate_damage_buffer():
    print("Item reward: x1 Damage Buffer\n")
    damage_buffer = Item("Damage Buffer", 10, 0, 0, "Increases damage by 50%.")
    allDamageBuffers.append(damage_buffer)


# Function that selects random item object generator.
def obtain_item():
    i = random.randint(0, 3)

    if i == 0:
        generate_normal_potion()

    elif i == 1:
        generate_large_potion()

    elif i == 2:
        generate_fire_flask()

    elif i == 3:
        generate_damage_buffer()


# Displays the user's inventory
def display_items():
    potion_amout = len(allNormalPotions)
    large_potion_amount = len(allLargePotions)
    fire_flask_amount = len(allFireFlasks)
    damage_buffer_amount = len(allDamageBuffers)

    print(f"{mainHero.heroName}'s inventory\n")

    number_list = [1, 2, 3, 4]

    if potion_amout > 0:
        print(f"{number_list[0]} — x{potion_amout} Potion: Heals for 10HP.")
        del number_list[0]

    if large_potion_amount > 0:
        print(f"{number_list[0]} — x{large_potion_amount} Large Potion: Heals for 20HP.")
        del number_list[0]

    if fire_flask_amount > 0:
        print(f"{number_list[0]} — x{fire_flask_amount} Fire Flask: Deals 20 damage.")
        del number_list[0]

    if damage_buffer_amount > 0:
        print(f"{number_list[0]} — x{damage_buffer_amount} Damage Buffer: Increases damage by 50%.")
        del number_list[0]

    if damage_buffer_amount <= 0 \
            and fire_flask_amount <= 0 \
            and large_potion_amount <= 0 \
            and potion_amout <= 0:
        print("No items")


inventory = [allNormalPotions, allLargePotions, allDamageBuffers, allFireFlasks]


def use_item(item):
    using_item = item
    print(f"\n{mainHero.heroName} used a {using_item.itemName}!")
    time.sleep(1.25)

    if item == normalPotion:
        temp_hp = mainHero.heroHP + normalPotion.itemHeal

        if temp_hp > maxHP:
            mainHero.heroHP = maxHP

        elif temp_hp <= maxHP:
            mainHero.heroHP = temp_hp

        print(f"{mainHero.heroName} gained {round(using_item.itemHeal)}HP!")
        time.sleep(1.25)
        print(f"{mainHero.heroName} has {round(mainHero.heroHP)}HP!\n")
        time.sleep(1.25)

        allNormalPotions.pop()

    elif item == largePotion:
        temp_hp = mainHero.heroHP + largePotion.itemHeal

        if temp_hp > maxHP:
            mainHero.heroHP = maxHP

        elif temp_hp <= maxHP:
            mainHero.heroHP = temp_hp

        print(f"{mainHero.heroName} gained {round(using_item.itemHeal)}HP!")
        time.sleep(1.25)
        print(f"{mainHero.heroName} has {round(mainHero.heroHP)}HP!\n")
        time.sleep(1.25)

        allLargePotions.pop()

    elif item == fireFlask:
        print(f"{mainHero.heroName} dealt {round(using_item.itemDmg)} damage to {enemy.enemyName}!")
        enemy.enemyHP -= fireFlask.itemDmg
        time.sleep(1.25)
        if enemy.enemyHP <= 0:
            time.sleep(0.75)
            print(str(enemy.enemyName) + " was defeadet!\n")
            time.sleep(1.25)

        elif enemy.enemyHP > 0:
            print(f"{enemy.enemyName} has {round(enemy.enemyHP)}HP left!\n")

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

        allFireFlasks.pop()

    elif item == damageBuffer:
        print(f"{mainHero.heroName}'s damage increased by 50%!\n")
        time.sleep(1.25)
        mainHero.heroDMG *= damageBuffer.itemBuff

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

        allDamageBuffers.pop()
