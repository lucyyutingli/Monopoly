# Monopoly Without the Pain
This quarantine season I played a few games of Monopoly with my friends online. They games were fun, but they were sometimes painstakingly long and there were moments where our friendships were on their last legs. I thought, "wouldn't it be great if you could play Monopoly without *playing* Monopoly?". That's when I got the idea to create a Monopoly simulation, that goes through an entire game of Monopoly with no human input other than the names of the players. This simulation would complete everything like dice rolls, property buying, etc. and players can just watch it happen through print messages on the screen. Instead of playing Monopoly for hours, you could watch it happen in minutes. I call this **Monopoly Without the Pain**.

This project was started on **9/11/2020** and is impelemented in **Python 3**.

## Requirements
This is both for the user and myself to keep track of gameplay aspects of Monopoly that will need to be included. The game of Monopoly is both simple and complex at the same time, so I wanted to focus on the most important aspects of the game first. Below are lists of mechanics and their possible implementations, which are subject to change as I work through the project. 

**Priority Game Mechanics**
- Layout of the Map (array or list)
- Player values including (class):
    - Location
    - Money Owned
    - Properties Owned
- Taking turns (booleans or a helper function such as "whose_turn")
- Rolling dice (rng)
- Buying properties/ownership (array of tuples within layout of map, or array within array)
- Property bonuses including:
    - Owning all of one color or set (collections?)
    - Buying houses -> hotels (boolean/max number)
    - Increasing rent each level (simple addition operator)
- Corner spaces (booleans):
    - Go to Jail
    - Just Visiting
    - Free Parking
    - Go

**Second Priority Game Mechanics**
- Mortgaging properties
- Trading
- Going bankrupt
- Chance spaces
