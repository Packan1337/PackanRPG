import collections
import random
import time


class Enemy:

    def __init__(self, enemy_name, enemy_hp, enemy_dmg):
        self.enemyName = enemy_name
        self.enemyHP = enemy_hp
        self.enemyDMG = enemy_dmg

    def __str__(self):
        return self.enemyName


enemyList = [Enemy("Bazaar Turk", 23, 3),
             Enemy("Fat Ass Swamp Monster", 15, 5),
             Enemy("Hairy Arab", 17, 3),
             Enemy("Huge Fucking Lizard", 15, 5),
             Enemy("Keyboard Warrior", 22, 5)]

# Enemy is chosen from a list of enemies.
enemy = random.choice(enemyList)


class Hero:

    def __init__(self, hero_name):
        self.heroName = hero_name
        self.heroHP = 25
        self.heroDMG = 10

    def __str__(self):
        return self.heroName


# Config file that saves user's name.
config = open("config.txt", "r")
name = config.read()
config.close()
mainHero = Hero(name)
maxHP = mainHero.heroHP


class Item:

    def __init__(self, item_name, item_heal, item_dmg, item_buff, item_desc):
        self.itemName = str(item_name)
        self.itemHeal = int(item_heal)
        self.itemDmg = int(item_dmg)
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


# TODO fix item obtain system
# Functions that generate new item object.
def generate_normal_potion():
    print("Item reward: x1 Normal Potion\n")
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

    if potion_amout > 0:
        print(f"x{potion_amout} Potion: Heals for 10HP.")

    if large_potion_amount > 0:
        print(f"x{large_potion_amount} Large Potion: Heals for 20HP.")

    if fire_flask_amount > 0:
        print(f"x{fire_flask_amount} Fire Flask: Deals 20 damage.")

    if damage_buffer_amount > 0:
        print(f"x{damage_buffer_amount} Damage Buffer: Increases damage by 50%.")

    if potion_amout < 0 and large_potion_amount < 0 and fire_flask_amount < 0 and damage_buffer_amount < 0:
        print("No items")


inventory = [allNormalPotions, allLargePotions, allDamageBuffers, allFireFlasks]


def use_item(item):
    using_item = item
    print(f"{mainHero.heroName} used a {using_item.itemName}!")
    time.sleep(1.25)

    if item == normalPotion:
        temp_hp = mainHero.heroHP + normalPotion.itemHeal

        if temp_hp > maxHP:
            mainHero.heroHP = maxHP

        elif temp_hp <= maxHP:
            mainHero.heroHP = temp_hp

        print(f"{mainHero.heroName} gained {using_item.itemHeal}!")
        time.sleep(1.25)
        print(f"{mainHero.heroName} has {mainHero.heroHP}!")
        time.sleep(1.25)

        allNormalPotions.pop()

    elif item == largePotion:
        temp_hp = mainHero.heroHP + largePotion.itemHeal

        if temp_hp > maxHP:
            mainHero.heroHP = maxHP

        elif temp_hp <= maxHP:
            mainHero.heroHP = temp_hp

        print(f"{mainHero.heroName} gained {using_item.itemHeal}!")
        time.sleep(1.25)
        print(f"{mainHero.heroName} has {mainHero.heroHP}!")
        time.sleep(1.25)

        allLargePotions.pop()

    elif item == fireFlask:
        print(f"{mainHero.heroName} dealt {using_item.itemDMG} damage to {enemy.enemyName}!")
        time.sleep(1.25)

        allFireFlasks.pop()

    elif item == damageBuffer:
        allDamageBuffers.pop()

