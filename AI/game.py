"""This file contains the main Game logic for fruitsweeper"""

import time
from gamemap import GameMap
from ai import AI


WIDTH = 10
MINES = 10
game_map = GameMap(MINES, WIDTH)
player = AI()
turns_counter = 0
init_time = time.time()

while not game_map.is_end_game():
    action = player.play(game_map.get_map_format())
    turns_counter += 1
    if action["action"] == "explore":
        game_map.explore(action["X"], action["Y"])
    else:
        if action["action"] == "flag":
            game_map.flag(action["X"], action["Y"])
        else:
            if action["action"] == "unflag":
                game_map.unflag(action["X"], action["Y"])

    print(game_map.to_string())

end_time = time.time()
elapsed_time = end_time - init_time

print("You won! in " + str(turns_counter) + " turns " +
      "and in " + str(elapsed_time) + " seconds")
