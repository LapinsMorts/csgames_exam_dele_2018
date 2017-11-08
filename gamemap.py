"""The fruitsweeper game map"""

import random
import copy
from tile import Tile


class GameMap(object):
    """The game map"""
    def __init__(self, mine_amount, width):
        self.__flagged = []
        self.__map_format = []
        self.__map = []
        self.__fruits = []
        self.__width = width
        random.seed()
        for i in range(width):
            self.__map.append([])
            for j in range(width):
                self.__map[i].append(Tile(i, j))
        k = 0
        while k < mine_amount:
            x_pos = random.randrange(0, width)
            y_pos = random.randrange(0, width)
            if [x_pos, y_pos] not in self.__fruits:
                self.__fruits.append([x_pos, y_pos])
                self.__map[x_pos][y_pos].contains_fruit = True
            else:
                k -= 1
            k += 1

        for i in range(width):
            for j in range(width):
                self.set_number(i, j)
        self.set_map_format()

    def to_string(self):
        """Returns the map as a stirng"""
        map_string = ""
        for i in range(self.__width):
            for j in range(self.__width):
                map_string += self.__map_format[i][j]
            map_string += "\n"
        return map_string

    def explore(self, x_pos, y_pos):
        """explores a tile of the map"""
        if not self.__map[x_pos][y_pos].explored:
            tmp = self.__map[x_pos][y_pos].reacts()  # will end game if contains fruit
            self.__map[x_pos][y_pos].explored = True
            self.__map_format[x_pos][y_pos] = str(
                self.__map[x_pos][y_pos].number)
            if tmp:
                self.flag(x_pos, y_pos)


    def flag(self, x_pos, y_pos):
        """Flags a tile of the map"""
        if [x_pos, y_pos] not in self.__flagged:
            self.__map[x_pos][y_pos].flagged = True
            self.__map_format[x_pos][y_pos] = "P"
            self.__flagged.append([x_pos, y_pos])


    def unflag(self, x_pos, y_pos):
        """Unflags a tile of the map"""
        if [x_pos, y_pos] in self.__flagged:
            self.__map[x_pos][y_pos].flagged = False
            self.__map_format[x_pos][y_pos] = "X"
            self.__flagged.remove([x_pos, y_pos])


    def set_number(self, x_pos, y_pos):
        """Finds the amount of fruits around a given tile"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and self.is_in_range(
                        x_pos, i, y_pos, j):
                    if self.__map[x_pos + i][y_pos + j].contains_fruit:
                        count += 1
        self.__map[x_pos][y_pos].number = count

    def is_in_range(self, x_pos, i_count, y_pos, j_count):
        """tells if a tile is in range of the map"""
        return (x_pos + i_count < self.__width and
                x_pos + i_count >= 0 and y_pos + j_count < self.__width and
                y_pos + j_count >= 0)

    def set_map_format(self):
        """Sets the map in an initial proper format"""
        for i in range(self.__width):
            self.__map_format.append([])
            for j in range(self.__width):
                self.__map_format[i].append("X")

    def get_map_format(self):
        """returns a deepcopy of the formated map"""
        return copy.deepcopy(self.__map_format)

    def is_end_game(self):
        """Compares the fruits and the flagged tiles to know if the
        game is finished"""
        return sorted(self.__fruits) == sorted(self.__flagged)
