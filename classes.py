

class Enemy:

    def __init__(self, enemy_name, enemy_hp, enemy_dmg):
        self.enemyName = enemy_name
        self.enemyHP = enemy_hp
        self.enemyDMG = enemy_dmg

    def __str__(self):
        return self.enemyName


enemyList = [Enemy("Baby Swamp Monster", 7, 3),
             Enemy("Swamp Monster", 15, 5),
             Enemy("Baby Lizard", 7, 3),
             Enemy("Lizard", 15, 5)]


class Hero:

    def __init__(self, hero_name):
        self.heroName = hero_name
        self.heroHP = 25
        self.heroDMG = 10

    def __str__(self):
        return self.heroName


config = open("config.txt", "r")
name = config.read()
config.close()
mainHero = Hero(name)


class Item:

    def __init__(self, item_name, item_heal, item_dmg, item_buff):
        self.item_name = item_name
        self.item_heal = item_heal
        self.item_dmg = item_dmg
        self.item_buff = item_buff


items = [Item("Potion", 10, 0, 0)]
