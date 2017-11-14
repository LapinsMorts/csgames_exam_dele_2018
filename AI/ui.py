import curses
from curses import wrapper
import time
from threading import Thread
import signal


x = 1
y = 1
winarray = []

def flash():
    while not stop_flashing:
        winarray[x][y].erase()
        winarray[x][y].refresh()
        time.sleep(0.3)
        winarray[x][y].addstr("X")
        winarray[x][y].refresh()
        time.sleep(0.3)

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()

    begin_x = 5; begin_y = 7
    height = 3; width = 6
    # map creation
    for i in range(11):
        winarray.append([])
        for j in range(11):
            winarray[i].append(curses.newwin(height, width, begin_y + i * height, begin_x + j * width))
            if i == 0 and j == 0:
                winarray[i][j].addstr("")
            else:
                if i == 0:
                    winarray[i][j].addstr(str(j-1))
                else:
                    if j == 0:
                        winarray[i][j].addstr(str(i-1))
                    else:
                        winarray[i][j].addstr("X")
            winarray[i][j].refresh()
    #curses.setsyx(begin_y, begin_x)
    #stdscr.refresh()
    curses.curs_set(0)

    th_flash.start()
    while True:
        a = stdscr.getkey()
    #    if a == KEY_RIGHT:


    #stdscr.getkey()
########################################################## to exit better

stop_flashing = False
th_flash = Thread(target=flash)


wrapper(main)
