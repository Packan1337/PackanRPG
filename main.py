# Main code for PackanRPG
# Written by Aria Kalantari aka Packan, 2022

from classes import Hero, Enemy
import fight, battle

# Main variables

print("\nWelcome to PackanRPG!")

heroName = Hero(input("First of all, what is your name?: "))
# attrs = vars(hero)

print("\n" + str(heroName) + ", I hope you're ready for the most mediocre RPG adventure of your lifetime!\n")

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

        state = int(input("1. Begin PackanRPG"))

elif state == 2:
    print("\nfuck you")
    exit()

# Test
