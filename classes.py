class Enemy:

    enemyName = str("")
    enemyHP = range(10, 25)
    enemyDMG = range(5, 12)


class Hero:

    def __init__(self, hero_name):
        self.heroName = hero_name
        self.heroHP = 25
        self.heroDMG = 10

    @classmethod
    def from_input(cls):
        return cls(
            input('First of all, what is your name?: ')
        )

    # heroName = str(input(""))
    # heroHP = int(25)
    # heroDMG = range(7, 15)
