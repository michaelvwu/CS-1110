# Michael Wu (mvw5mf)
import random

print("Welcome to Pig!")

player = 0
computer = 0

total_player = player
total_computer = computer

turn = 'y'
switch = False

# roll = random.randint(1,6)

while total_player != 100 or total_computer != 100:
    while switch is False:
        roll = random.randint(1, 6)
        print("Player:", total_player, "Computer:", total_computer)
        if roll != 1:
            if turn == 'n':
                total_player = player
                player += roll
                print("Your total score is now:", total_player)
                switch = True

            elif turn == 'y':
                print("It's your turn!")
                player += roll
                print("you rolled a", roll)
                print("You currently have", str(player), "banked")

        else:
            total_player = 0
            player = 0
            print("you rolled a", roll)
            print("PIG! Too Bad! Your total is currently:", total_player)
            switch = True


        if switch is False:
            turn = input("Do you wish to roll again (y/n)?: ")
            print(" ")
        else:
            switch = True

    while switch is False:
        roll = random.randint(1, 6)
        print("Player:", total_player, "Computer:", total_computer)
        if roll != 1:
             if turn == 'n':
                total_computer = computer
                computer += roll
                print("Your total score is now:", total_computer)
                switch = True
             elif turn == 'y':
                print("It's your turn!")
                computer += roll
                print("you rolled a", roll)
                print("You currently have", str(computer), "banked")

        else:
            total_computer = 0
            computer = 0
            print("you rolled a", roll)
            print("PIG! Too Bad! Your total is currently:", total_computer)
            switch = False


        if roll != 1:
            turn = input("Do you wish to roll again (y/n)?: ")
            print(" ")
        else:
            switch = False


    if total_computer >= 100:
        print("The computers wins!", total_computer, "to", total_player)
    elif total_player >= 100:
        print("The player wins!", total_player, "to", total_computer)
    break