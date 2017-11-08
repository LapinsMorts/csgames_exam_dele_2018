"""Contains the Tile class, used to build a map in
fruitsweeper"""


class Tile(object):
    """Consists of a tile of the fruitsweeper game"""

    def __init__(self, x_pos, y_pos, contains_fruit=False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.contains_fruit = contains_fruit
        self.explored = False
        self.flagged = False
        self.number = 0

    def to_string(self):
        """Returns the tile represented as a string"""
        if self.explored:
            return str(self.number)
        if self.flagged:
            return "P"
        return "X"

    def reacts(self):
        """Checks if the player loses"""
        if self.contains_fruit:
            print("REACTION ALLERGIQUE!!! YOU LOST NOOB")
            exit()

