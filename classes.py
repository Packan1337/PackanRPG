import collections
import random
from collections import Counter


class Enemy:

    def __init__(self, enemy_name, enemy_hp, enemy_dmg):
        self.enemyName = enemy_name
        self.enemyHP = enemy_hp
        self.enemyDMG = enemy_dmg

    def __str__(self):
        return self.enemyName


enemyList = [Enemy("Bazaar Turk", 11, 3),
             Enemy("Fat Ass Swamp Monster", 15, 5),
             Enemy("Hairy Arab", 11, 3),
             Enemy("Huge Fucking Lizard", 15, 5),
             Enemy("Keyboard Warrior", 22, 5)]


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


class Item:

    def __init__(self, item_name, item_heal, item_dmg, item_buff, item_desc):
        self.itemName = str(item_name)
        self.itemHeal = float(item_heal)
        self.itemDmg = float(item_dmg)
        self.itemBuff = float(item_buff)
        self.itemDesc = str(item_desc)

    def __repr__(self):
        return str(self.itemName), str(self.itemDesc)


# Available items in the game.
itemList = [Item("Normal Potion", 10, 0, 0, "Heals 10HP"),
            Item("Large Potion", 20, 0, 0, "Heals 20HP"),
            Item("Fire Flask", 0, 10, 0, "Deals 10 damage to enemy"),
            Item("Damage Buffer", 0, 0, 1.5, "Increases damage with 50%")]


# Unique lists for each item.
allNormalPotions = []
allLargePotions = []
allFireFlasks = []
allDamageBuffers = []


# TODO fix item obtain system
# Functions that generate new item object.
def generate_normal_potion():
    print("Item reward: x1 Normal Potion\n")
    allNormalPotions.append(itemList[0])


def generate_large_potion():
    print("Item reward: x1 Large Potion\n")
    allNormalPotions.append(itemList[1])


def generate_fire_flask():
    print("Item reward: x1 Fire Flask\n")
    allNormalPotions.append(itemList[2])


def generate_damage_buffer():
    print("Item reward: x1 Damage Buffer\n")
    allNormalPotions.append(itemList[3])


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


# User's inventory.
inventory = [allNormalPotions, allLargePotions, allDamageBuffers, allFireFlasks]

# TODO fix function that deletes item from inventory after usage


# Get total amount of items.


# User recieves item after battle.
