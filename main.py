# Written by Packan, 2022
from classes import *
from battle import battle

print("\nWelcome to PackanRPG!")
# Writing user's name in config.txt file.
# TODO fix buffer error when writing user's name to config.txt

mainHero.heroName = input("First of all, what is your name?: ")

time.sleep(0.5)
print("\nSaving", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".")
time.sleep(1)

print("\n" + mainHero.heroName + ", I hope you're ready for the most mediocre RPG adventure of your lifetime!\n")

print("The menu system is very simple.")
print("You will choose between a few numbers in order to select different options.")
print("Type the corresponding number and hit enter to select.\n")

state = int(input("1. I understand\n2. I don't understand because I am stupid\n\n"))

if state == 1:
    print("\nGreat!")
    print("Would you like to begin PackanRPG or read about the battle system?\n")
    state = int(input("1. Begin PackanRPG\n2. Read about the battle system\n\n"))

    if state == 1:
        print("\nPackanRPG now starting...")

    elif state == 2:
        print("\nInformation about the battle system")
        print("It's like Pokémon but worse\n")

        state = int(input("1. Begin PackanRPG\n\n"))

elif state == 2:
    battle()

    exit()
