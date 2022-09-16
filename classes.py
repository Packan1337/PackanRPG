class Enemy:

    def __init__(self, enemy_name, enemy_hp, enemy_dmg):
        self.enemyName = enemy_name
        self.enemyHP = enemy_hp
        self.enemyDMG = enemy_dmg

    def __str__(self):
        return self.enemyName


enemyList = [Enemy("Baby Swamp Monster", 11, 3),
             Enemy("Swamp Monster", 15, 5),
             Enemy("Baby Lizard", 11, 3),
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

    def __init__(self, item_name, item_heal, item_dmg, item_buff, item_desc):
        self.itemName = str(item_name)
        self.itemHeal = float(item_heal)
        self.itemDmg = float(item_dmg)
        self.itemBuff = float(item_buff)
        self.itemDesc = str(item_desc)

    def __repr__(self):
        return str(self.itemName), str(self.itemDesc)

    def __str__(self):
        return str(self.itemName) + ": " + str(self.itemDesc)


items = [Item("Potion", 10, 0, 0, "Heals 10HP"),
         Item("Potion XL", 20, 0, 0, "Heals 20HP"),
         Item("Fire flask", 0, 10, 0, "Deals 10 damage to enemy"),
         Item("Damage buffer", 0, 0, 1.5, "Increases damage with 50%")]


inventory = [Item("Potion", 10, 0, 0, "Heals 10HP"),
             Item("Fire flask", 0, 10, 0, "Deals 10 damage to enemy"),
             Item("Damage buffer", 0, 0, 1.5, "Increases damage with 50%")]
