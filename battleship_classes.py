
#Making a game of Battleship
#Actors: Player, Ships, Board, Game
#actions: place ship, track ship, fire shot

#Player: place ships at start of the game, fire shots at other player.
#   Collab: Board, Ships, Game

#Ships: track health, track position?
#   collab: player, board

#Board: take input from players for firing shots, may track ship position?, keep track how many ships each player has remaining
#   collab: Ships, player, game

#Game: controls player turns
#   collab: board, players


#Start of Ship class

class Ship:

    def __init__(self, size, type):
        self.size = size
        self.type = type

    def __str__(self):
        pass

#Start of Player Class

class Player:

    def __init__(self, name):
        self.name = name
        self.destroyer = Ship(2, "Destroyer")
        self.cruiser = Ship(3, "Cruiser")
        self.sub = Ship(3, "Submarine")
        self.battleship = Ship(4, "Battleship")
