# Module for fight option in battle
import random

dmg = random.randint(3, 10)

open("config.txt", "r")

def fight(hero, heroHp, enemy, enemyHp):
    print(hero + " attacks " + enemy + "!")
    print(enemy + " lost " + dmg + "HP!")

    if enemyHp > 0:
        print(enemy + " attacks " + hero + "!")
        print(hero + "lost" + heroHp + "HP!")