from view import Core
from view import Constants

import curses


menu = [" New Game ", " Resume Existing Counter "]


def init(window):
    window.bkgd(curses.color_pair(2))
    window.clear()
    window.box()
    window.keypad(True)

    window.addstr(0, 2, "MENU")

    current_row = 0
    printMenu(window, current_row)

    while True:
        key = window.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                return Constants.NEW_GAME
            else:
                return Constants.RESUME_GAME
        elif Core.checkFinish(key):
            return key

        printMenu(window, current_row)


def printMenu(window, selected_row_idx):
    h, w = window.getmaxyx()

    for idx, row in enumerate(menu):
        x = int(w/2 - len(row)/2)
        y = int(h/2 - len(menu)/2 + idx)
        if idx == selected_row_idx:
            window.attron(curses.color_pair(3))
            window.addstr(y, x, row)
            window.attroff(curses.color_pair(3))
        else:
            window.addstr(y, x, row)
