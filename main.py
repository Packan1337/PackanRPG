# Written by Packan, 2022
from classes import *
from battle import battle

time.sleep(1)
print("\nWelcome to PackanRPG!")
time.sleep(1)

# This was written before I knew about f-strings lol
mainHero.heroName = input("First of all, what is your name?: ")
time.sleep(0.5)
print("\nSaving", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".")
time.sleep(1)

print("\n" + mainHero.heroName + ", I hope you're ready for the most mediocre RPG adventure of your lifetime!\n")
time.sleep(3)
print("The menu system is very simple.")
time.sleep(2)
print("You will choose between a few numbers in order to select different options.")
time.sleep(3)
print("Type the corresponding number and hit enter to select.\n")
time.sleep(2)

while True:
    try:
        print("1. I understand\n2. I don't understand because I am stupid\n")
        state = int(input("Option: "))

        if state != 1 and state != 2:
            print("\n(Select by using a valid number!)\n")
            time.sleep(1.25)

        if state == 1 or state == 2:
            break

    except ValueError:
        print("\n(Select by using a valid number!)\n")
        time.sleep(1.25)


if state == 1:
    print("\nGreat!")
    time.sleep(1)
    print("Would you like to begin PackanRPG or read about the battle system?\n")

    while True:
        try:
            time.sleep(1.25)
            print("1. Begin PackanRPG\n2. Read about the battle system\n")
            state = int(input("Option: "))

            if state != 1 and state != 2:
                print("\n(Select by using a valid number!)\n")

            if state == 1 or state == 2:
                break

        except ValueError:
            print("\n(Select by using a valid number!)\n")



    if state == 1:
        print("\nPackanRPG now starting", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".\n")
        time.sleep(1)

    elif state == 2:
        print("\nInformation about the battle system")
        time.sleep(1)
        print("It's like Pokémon", end="")
        time.sleep(1.5)
        print(" but worse\n")
        time.sleep(1)

        print("1. Begin PackanRPG\n")
        state = int(input("Option: "))

        print("\nPackanRPG now starting", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".\n\n")
        time.sleep(1)

elif state == 2:
    print("\nfuck you")
    time.sleep(2)
    exit()


print("Let's start with an enemy encounter.")
time.sleep(2)
print("Enemies are weak, but will scale up in difficulty as you level up.")
time.sleep(3)
print("Good luck, have fun!")
time.sleep(2)
battle()

time.sleep(1)
while True:
    print("\nYou are playing an alpha version of PackanRPG.")
    print("There is not much more to play yet.")
    print("Would you like to do another battle?\n")
    print("1. Another battle\n2. Exit PackanRPG\n")
    extra_option = int(input("Option: "))

    if extra_option == 1:
        battle()
    else:
        exit()
