import random  # for dice rolls
from collections import defaultdict
# All helper functions separated by the parts of the code they assist with

# -----------------------------------------------------PLAYER ORDER -------------------------------------------------------------------------
# Creates a new list of player's rolls


def new_roll_list(player_listed):
    player_rolls = []

    for i in player_listed:
        roll = random.randint(2, 12)
        player_rolls.append((roll, i))
    return player_rolls

# Creates a new dictionary of player's rolls. Key: Value, is Rolled Number: Players who rolled the number


def new_roll_dict(roll_list):
    player_roll_defaultdict = defaultdict(list)

    for i in roll_list:
        player_roll_defaultdict[i[0]].append(i[1])

    player_roll_dict = (player_roll_defaultdict)
    player_roll_new_dict = defaultdict(list)

    for i in sorted(player_roll_dict.keys(), reverse=True):
        player_roll_new_dict[i].append(player_roll_dict.get(i))
    return player_roll_new_dict

# A function to check for duplicates within a roll dictionary


def duplicate_check(player_num: int, rolls: dict, returned_list: list):
    unique = 0
    while(unique != player_num):
        for i in rolls:
            num_dup_players = len(rolls.get(i))
            if num_dup_players > 1:
                print("The following players got a duplicate roll of {}: {}. Resolving between the players...".format(
                    i, rolls.get(i)))
                dup_roll_dict = new_roll_dict(new_roll_list(num_dup_players))
                duplicate_check(num_dup_players, dup_roll_dict,
                                roll_order, returned_list)

            else:
                returned_list.append(rolls.get(i)[0][0])
                unique += 1
    return returned_list

# --------------------------------------- LOCATION DETERMINATION -------------------------------


def double_checker(num_doubles: int):
    # First double
    if num_doubles == 0:
        num_doubles += 1
        print("{} got a double!".format(player.dict["name"]))
        return num_doubles
    # Second double
    elif num_doubles == 1:
        num_doubles += 1
        print("{} got another double! One more and they get jail time!".format(
            player.dict["name"]))
        return num_doubles
    # Third double
    elif num_doubles == 2:
        num_doubles += 1
        print("{} got a third double! To jail with them!".format(
            player.dict["name"]))
        return num_doubles
        

# --------------------------------------- TAKING THEIR TURNS --------------------------------------------------------------


def property_bonus_check(player_name):
    pass


def determine_rent(property):
    pass
