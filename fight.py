# Module for fight option in battle
import random
from classes import Hero, Enemy


def fight():
    print(Hero.heroName + " attacks " + Enemy.enemyName + "!")
    print(Enemy.enemyName + " lost " + Hero.heroDMG + "HP!")

    if Enemy.enemyHP > 0:
        print(Enemy.enemyName + " attacks " + Hero.heroName + "!")
        print(Hero.heroName + "lost" + Enemy.enemyDMG + "HP!")
