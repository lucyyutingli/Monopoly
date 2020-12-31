#Imports! ---------------------------------------------------------------------------------------------
import pyfiglet # for ascii art
# import random # for dice rolls
# from collections import defaultdict # for determining roll order
from classes_and_variables import * # I realize this is discouraged, but this was all originally in one file so I know names won't conflict
from helper_functions import *

# Classes and variables in the file named "classes_and_variables"
# Helper functions in file named "helper_functions"

# --------------------------------------------------------------------------------- OPENER ----------------------------------------------------------------

banner = pyfiglet.figlet_format("WELCOME TO MONOPOLY (without the pain)")
print(banner)

players_entered = False
player_list = []

# Getting player(s) information (and a bit of cheeky flaming). Hard-coded for now, I'll try to figure out how to make this flexible in a later version
while (players_entered == False):
    try:
        playernum = int(input("How many players are playing? (Supports 2-4 players): "))
        print("\n")
    except ValueError:
        print("Hey, this input isn't allowed. This is an integer only zone! Try again.\n")
        continue
    if playernum == 1:
        print("Look, I get it, you wanna play by yourself, but that's not how this game works! This isn't Solitaire! " 
                "Where's the fun in playing by yourself anyways? Sounds awfully lonely. Try again.\n")

    elif playernum == 2:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Plase type in player 2's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2


        player_list.extend([player1, player2])

    elif playernum == 3:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Please type in player 2's name: ")
        name3 = input("Please type in player 3's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()
        player3 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2
        player3.dict["name"] = name3

        player_list.extend([player1, player2, player3])

    elif playernum == 4:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Please type in player 2's name: ")
        name3 = input("Please type in player 3's name: ")
        name4 = input("Please type in player 4's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2
        player3.dict["name"] = name3
        player4.dict["name"] = name4

        player_list.extend([player1, player2, player3, player4])

        players_entered = True

    else:
        print("Surprise surprise, you put in an unsupported number of players and found this cheeky message! Congrats. Try again.\n")

print ("\nThank you, the game will now begin. May the (RNG) odds be ever in your favor. \n")

# --------------------------------------------------------------------------- DETERMINING PLAYER ORDER ----------------------------------------------------------------
""" This whole section seems a little more complicated than it needs to be right now, I will probably come back to it later.
    You can check out all the functions I use here in the helper_function.py file """

print("Determining turn order...\n")

# Create rolls, check for duplicates, return player order 
player_rolls = new_roll_list(player_list)

print("Original rolls listed:")
for i in player_rolls:
    print("{} got a roll of {}. ".format(i[1].dict["name"], i[0]))

print("\n")

player_roll_dict = new_roll_dict(player_rolls)

final_roll_order = duplicate_check(playernum, player_roll_dict, [])


# Final player order
print("The player order will be as follows: ")
for i in final_roll_order:
    print(i.dict["name"])

# ---------------------------------------------------------------------------- MAIN GAME FUNCTIONS -------------------------------------------------------------------
""" Playing the actual game! Yay! We made it! """


players_in = playernum 

while players_in > 1:
    # Variables
    dice_one = 0
    dice_two = 0
    total_roll = 0
    doubles = 0

    # One player's whole turn ---------------------------------------
    # Calculating player's dice roll
    for player in final_roll_order:
        finished == False
        while (finished == False)
            dice_one = random.randint(1,6)
            dice_two = random.randint(1,6)
            total_roll = dice_one + dice_two
            current_loc = None
            location_number = board.index(player.dict["location"])

            print("{} got a roll of {} and {} for a total of {}".format(player.dict["name"], dice_one, dice_two, total_roll))

            # Checking out some doubles
            if dice_one == dice_two:
            doubles = double_checker(doubles)
                    
            # New location determiner   
            if doubles == 3:
                location_number = 10
                player.dict["location"] = board[location_number]
                break
            elif location_number + total_roll > 39:
                location_number = location_number + total_roll - 39 - 1
            else:
                location_number += total_roll

            player.dict["location"] = board[location_number]
            current_loc = board[location_number]

            
            # Purchasing some properties
            if current_loc.owner == "None":
                player.dict["money"] -= current_loc.init_cost
            else:
                curr_loc_owner = current_loc.owner







