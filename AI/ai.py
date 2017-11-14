"""The AI file that people have to complete"""

import time

class AI(object):
    """An instance of AI will try to solve the
    fruitsweeper"""

    def __init__(self):
        self.__return_x = -1
        self.__return_y = -1

    def play(self, game_map):
        """You must complete this function and return
        a dictionnary following the format:
            {"action":"[(explore)(flag)(unflag)]", "X":0, "Y": 0}
        game_map is a list of lists of string which contains the details
        of the tile: X is for unexplored tile, P is for a flagged tile
        and a number represents the amount of tiles containing a fruit
        surrounding the tile
        """
        self.__return_x = (self.__return_x + 1) % len(game_map)
        if self.__return_x == 0:
            self.__return_y += 1

        time.sleep(0.1)
#        self.__return_x = int(input())
#        self.__return_y = int(input())

        return {"action":"explore",
                "X":self.__return_x,
                "Y":self.__return_y
               }
