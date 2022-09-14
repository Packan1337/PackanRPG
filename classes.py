class Enemy:

    def __init__(self, enemy_name):
        self.enemyName = enemy_name
        self.enemyHP = range(10, 25)
        self.enemyDMG = range(5, 12)

    def __str__(self):
        return self.enemyName


class Hero:

    def __init__(self, hero_name):
        self.heroName = hero_name
        self.heroHP = 25
        self.heroDMG = 10

    def __str__(self):
        return self.heroName

    @classmethod
    def from_input(cls):
        return cls(
            input('First of all, what is your name?: ')
        )

    # heroName = str(input(""))
    # heroHP = int(25)
    # heroDMG = range(7, 15)
