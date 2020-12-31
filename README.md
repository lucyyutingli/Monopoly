# Monopoly Without the Pain
This quarantine season I played a few games of Monopoly with my friends online. They games were fun, but they were sometimes painstakingly long and there were moments where our friendships were on their last legs. I thought, "wouldn't it be great if you could play Monopoly without *playing* Monopoly"? That's when I got the idea to create a Monopoly simulation, that goes through an entire game of Monopoly with no human input other than the names of the players. This simulation would complete everything like dice rolls, property buying, etc. and players can just watch it happen through print messages on the screen. Instead of playing Monopoly for hours, you could watch it happen in minutes. I call this **Monopoly Without the Pain**.

This project was started on **9/11/2020** and is impelemented in **Python 3**. As always, please let me know if you have any suggesstions for improvement. I am always open to comments and critiques!

## **Requirements**
This is both for the user and myself to keep track of gameplay aspects of Monopoly that will need to be included. The game of Monopoly is both simple and complex at the same time, so I wanted to focus on the most important aspects of the game first. Below are lists of mechanics and their possible implementations, which are subject to change as I work through the project. 

 **Priority Game Mechanics**
- Layout of the Map (array or list, I'm thinking about splitting the map into 4 in order to make running the program more effecient)
- Player values including (class):
    - Location
    - Money Owned
    - Properties Owned
- Taking turns (booleans or a helper function such as "whose_turn")
- Rolling dice (rng)
    - Doubles
    - Go to jail if triple doubles (simple counter)
- Buying properties/ownership (array of tuples within layout of map, or array within array)
- Property bonuses including:
    - Owning all of one color or set (collections?)
    - Buying houses -> hotels (boolean/max number)
    - Not allowing more houses to be bought unless each property in a color set has the same amount of houses
    - Increasing rent each level (simple addition operator)
- Corner spaces (booleans):
    - Go to Jail
    - Just Visiting
    - Free Parking
    - Go (add 200$ to player's money every pass)
- Chance spaces:
    - Community chest
    - Chance
    - Income tax
    - Luxury tax


 **Second Priority Game Mechanics**
- Mortgaging properties
- Going bankrupt
- Using held cards (get of jail free card, etc.)

## **Omitted Game Mechanics and Assumptions**
There are some game mechanics that don't really make sense when running a complete simulation of Monopoly. These include the following:
- Trading
    - If I want to have this experience completely user free, other than the names, I need to leave out any places where players could potentially change the path of the game. I don't have experience in AI (yet), so I at the moment I can't come up with an algorithm that could possibly guess what a player would do. However, if I was to make a second version of this project, I could potentially add options to trade when the opportunity arrises.
- Getting out of jail
    - There are moments in late-game of Monopoly where players want to acutally stay in jail in order to avoid having to pay higher rent fees. In this version, I am going to be assuming that players will want to get out of jail as soon as possible. A later version could include an algorithm that decides whether or not to stay in jail. For this version, I will have players pay the 50$ to leave jail, unless they do not have the money, in which they will roll to attempt to be free. 
- Buying as many houses and hotels as possible
    - My algorithm will assume that players will want to buy as many hotels and houses as possible, without going bankrupt. In this version, no one will buy houses or hotels until ALL properties have been purchased. After this condition, players will buy as many houses and hotels as possible, without going bankrupt. I will assume each player will want to keep at least 200$ in their pocket after purchases, which will increase by 50$ after all player finishes their turn for that round. 
- Once you are out of money, YOU LOSE
    - In order to keep things a little simpler, once you are out of money, you will declare bankruptcy and transfer all of your properties to the player you own money to. It's not very elegant, but I might want to add mortgaging to a version with more player control. 

## Required Downloaded Packages
- Pyfiglet

# Future Version Features
Listed here are a few things that I would want to add to a future version, if I decided to pursue one. This one would inevitably have more player control, but still mostly up to computer chance. 

- Mortgaging
- Trading
- Trading to stay in the game when you're out of money