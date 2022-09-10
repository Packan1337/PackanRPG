# Main code for PackanRPG
# Written by Aria Kalantari aka Packan, 2022
import random

# Main variables
state = 0

hero = ""
heroHp = 25

print("\nWelcome to PackanRPG!")
hero = (input("Before we begin, what is your name?: "))

print("\n" + hero + ", I hope you're ready for the most mediocre RPG adventure of your lifetime!\n")

print("The menu system is very simple.")
print("You will choose between a few numbers in order to select different options.")
print("Type the corresponding number and hit enter to select.\n")

state = input("1. I understand\n2. I don't understand because I am stupid\n\n")

if state == 1:
    print("Great!")
    print("Would you like to begin PackanRPG or read about the battle system?\n")
    state = input("1. Begin PackanRPG\n2. Read about the battle system\n\n")

    if state == 1:
        print("PackanRPG now starting...")

    elif state == 2:
        print("Information about the battle system")

elif state == 2:
    print("fuck you")
    exit()

