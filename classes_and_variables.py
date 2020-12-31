
# Classes and hard-coded information -------------------------------------------------------------------
# Player class that keeps track of a player's name, money, propeties, and held cards
class Player:
    def __init__(self):
        self.dict = {"name": "None", "money": 1500, "owned_props": {}, "cards":[], "location": board[0], "railroads": 0, "utilities": 0}

# Property class that keeps track of all of a properties rent and ownership. Names aren't needed here since we won't be doing any trading in this version, and they are 
# encapsulated within variable names.
class Colored_Properties:
    def __init__(self, color, init_cost, rent, house_cost, hotel_cost):
        self.color = color
        self.init_cost = init_cost # Initial cost of the property
        self.rent = rent #Order is as follows [Base Rent, One House Rent, Two House Rent, Three House Rent, Four House Rent, Hotel Rent]
        self.house_cost = house_cost # Cost of a house
        self.hotel_cost = hotel_cost # Cost of a hotel
        self.owner = "None"
        self.current_houses = 0
        self.property_bonus = False

class Railroads:
    def __init__(self):
        self.cost = 200
        self.rent = 25
        self.owner = "None"

class Utilities:
    def __init__(self):
        self.cost = 150
        self.owner = "None"


# Initizliaing all properties. Names will be replaced with characater numbers to bring down run time and memory required.
# Note the following:
#   - Monopoly rents are double the normal rent for colored properties
#   - Mortgages are half the intial cost
#   - Chance spaces don't need their own class or variable, it will be a simple check


# Browns
med_ave = Colored_Properties("0", 60, [2, 10, 30, 90, 160, 250], 50, 50)
bal_ave = Colored_Properties("0", 60, [4, 20, 60, 180, 320, 450], 50, 50)

# Light blues
ori_ave = Colored_Properties("1", 100, [6, 30, 90, 270, 400, 550], 50, 50)
ver_ave = Colored_Properties("1", 100, [6, 30, 90, 270, 400, 550], 50, 50)
conn_ave = Colored_Properties("1", 120, [8, 40, 100, 300, 450, 600], 50, 50)

# Pinks
stch_pl = Colored_Properties("2", 140, [10, 50, 150, 250, 625, 750], 100, 100)
st_ave = Colored_Properties("2", 140, [10, 50, 150, 250, 625, 750], 100, 100)
vir_ave = Colored_Properties("2", 160, [12, 60, 180, 500, 700, 900], 100, 100)

# Oranges
stjm_pl = Colored_Properties("3", 180, [14, 70, 200, 550, 750, 950], 100, 100)
ten_ave = Colored_Properties("3", 180, [14, 70, 200, 550, 750, 950], 100, 100)
ny_ave = Colored_Properties("3", 200, [16, 80, 220, 600, 800, 1000], 100, 100)

# Reds
ken_ave = Colored_Properties("4", 220, [18, 90, 250, 700, 875, 1050], 110, 150)
in_ave = Colored_Properties("4", 220, [18, 90, 250, 700, 875, 1050], 110, 150)
ill_ave = Colored_Properties("4", 240, [20, 100, 300, 750, 925, 1100], 120, 150)

# Yellows
at_ave = Colored_Properties("5", 260, [22, 110, 330, 800, 975, 1150], 130, 150)
ven_ave = Colored_Properties("5", 260, [22, 110, 330, 800, 975, 1150], 130, 150)
mar_gar = Colored_Properties("5", 280, [24, 120, 360, 850, 1025, 1200], 150, 150)

# Greens
pac_ave = Colored_Properties("6", 300, [26, 130, 390, 900, 1100, 1275], 200, 200)
nc_ave = Colored_Properties("6", 300, [26, 130, 390, 900, 1100, 1275], 200, 200)
penn_ave = Colored_Properties("6", 320, [150, 450, 1000, 1200, 1400], 200, 200)

# Dark blues
pa_pl = Colored_Properties("7", 350, [35, 175, 500, 1100, 1300, 1500], 200, 200)
bw = Colored_Properties("7", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200)

# Railroads
read_rail = Railroads()
penn_rail = Railroads()
bo_rail = Railroads()
sl_rail = Railroads()

# Utilities
ec = Utilities()
ww = Utilities()

# A list of all properties, grouped 
property_dict = {"0": [med_ave, bal_ave],
                 "1": [ori_ave, ver_ave, conn_ave],
                 "2": [stch_pl, st_ave, vir_ave],
                 "3": [stjm_pl, ten_ave, ny_ave],
                 "4": [ken_ave, in_ave, ill_ave],
                 "5": [at_ave, ven_ave, mar_gar],
                 "6": [pac_ave, nc_ave, penn_ave],
                 "7": [pa_pl, bw] }



# BOARD
# I originally wanted to break up the board into 4 different arrays to save on runtime and memory, but after trying to iterate
# through this kind of setup, I realized it was difficult to do so. I might try to figure out a different method at a later time. 
# Breaking up the board into 4 arrays. There is no possible way you cannot hard-code the Monopoly board, because it never changes. 
board = ["Go", med_ave, "Community Chest", bal_ave, "Income Tax", read_rail, ori_ave, "Chance", ver_ave, conn_ave, # first section
        "Jail", stch_pl, ec, st_ave, vir_ave, penn_rail, stjm_pl, "Community Chest", ten_ave, ny_ave, #second section
        "Free Parking", ken_ave, "Chance", in_ave, ill_ave, bo_rail, at_ave, ven_ave, ww, mar_gar, # third section
        "Go to Jail", pac_ave, nc_ave, "Community Chest", penn_ave, sl_rail, "Chance", pa_pl, "Luxury Tax", bw, "Go"] # fourth section

