import curses
from curses import wrapper
import time
from threading import Thread
import signal
from gamemap import GameMap
from ai import AI





"""
def flash():
    while not stop_flashing:
        winarray[x][y].erase()
        winarray[x][y].refresh()
        time.sleep(0.3)
        winarray[x][y].addstr("X")
        winarray[x][y].refresh()
        time.sleep(0.3)"""

def main(stdscr):
    def update(winarray, x, y, string):
        winarray[x][y].erase()
        winarray[x][y].addstr(0, 1, string)
        winarray[x][y].refresh()

    WIDTH = 10
    MINES = 10
    game_map = GameMap(MINES, WIDTH)
    player = AI()
    turns_counter = 0
    init_time = time.time()

    stdscr.clear()
    stdscr.refresh()

    winarray = []
    begin_x = 5; begin_y = 7
    height = 3; width = 6

    # UI creation




    borders = [];
    borders.append(curses.newwin(height * 11, width, begin_y , begin_x))
    borders[0].border(0)
    borders[0].refresh()
    borders.append(curses.newwin(height, width * 11 +1, begin_y , begin_x))
    borders[1].border(0)
    borders[1].refresh()

    for i in range(11):
        winarray.append([])
        for j in range(11):
            winarray[i].append(curses.newwin(1, 5, begin_y + 1 + i * height, begin_x  + 1 + j * width))
            if i == 0 and j == 0:
                winarray[i][j].addstr("")
            else:
                if i == 0:
                    winarray[i][j] = curses.newwin(1, 5, begin_y + 1 + i * height, begin_x  + 1 + j * width)
                    winarray[i][j].addstr(0, 2, str(j-1))
                else:
                    if j == 0:
                        winarray[i][j] = curses.newwin(1, 3, begin_y + 1 + i * height, begin_x  + 1 + j * width)
                        winarray[i][j].addstr(0, 1, str(i-1))
                    else:
                        winarray[i][j].addstr(0,2,"X")
            winarray[i][j].refresh()

    curses.curs_set(0)
    x = 1
    y = 1

    while not game_map.is_end_game():
        map_format = game_map.get_map_format()
        a = stdscr.getkey()
        update(winarray, x, y, " " + map_format[x-1][y-1])
        if a == "KEY_RIGHT":
            y += 1
        if a == "KEY_LEFT":
            y -= 1
        if a == "KEY_UP":
            x -= 1
        if a == "KEY_DOWN":
            x += 1
        if x <= 0:
            x = 1
        if x > 10:
            x = 10
        if y > 10:
            y = 10
        if y <= 0:
            y = 1
        action = ""
        if a == "e":
            action="explore"
        if a == "f":
            action = "flag"
        if a == "u":
            action == "unflag"
        input_obj = {"action":action, "X":(x-1), "Y": (y-1)}
        action = player.play(map_format, input_obj)
        turns_counter += 1
        if action["action"] == "explore":
            game_map.explore(action["X"], action["Y"])
            map_format = game_map.get_map_format()
            update(winarray, action["X"]+1, action["Y"]+1, " " + map_format[action["X"]][action["Y"]])
        else:
            if action["action"] == "flag":
                game_map.flag(action["X"], action["Y"])
                map_format = game_map.get_map_format()
                update(winarray, action["X"]+1, action["Y"]+1, " " + map_format[action["X"]][action["Y"]])
            else:
                if action["action"] == "unflag":
                    game_map.unflag(action["X"], action["Y"])
                    map_format = game_map.get_map_format()
                    update(winarray, action["X"]+1, action["Y"]+1, " " + map_format[action["X"]][action["Y"]])


        update(winarray, x, y, "_" + map_format[x-1][y-1]+"_")








wrapper(main)
