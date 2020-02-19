from view import Core
from view import Constants
from service import Storage

import curses
from os import listdir


def init(window):
    window.bkgd(curses.color_pair(2))
    window.clear()
    window.box()
    window.keypad(True)

    window.addstr(0, 2, "RESUME GAME")

    games = [f for f in listdir('ExistingGames/') if f.endswith(".p")]

    if len(games) == 0:
        noGames = 'There exist no games at the moment'
        createGame = 'Return to the menu by pressing any key'

        h, w = window.getmaxyx()
        y = int(h / 2)

        window.attron(curses.color_pair(3))

        x = int(w / 2 - len(noGames) / 2)
        window.addstr(y - 1, x, noGames)

        x = int(w / 2 - len(createGame) / 2)
        window.addstr(y, x, createGame)

        window.attroff(curses.color_pair(3))

        window.getch()
        return None, Constants.MENU
    else:
        currentRow = 0
        printFiles(window, currentRow, games)

        while True:
            key = window.getch()

            if key == curses.KEY_UP and currentRow > 0:
                currentRow -= 1
            elif key == curses.KEY_DOWN and currentRow < len(games) - 1:
                currentRow += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                game = Storage.load(games[currentRow])
                return game, Constants.NO_ACTION
            elif Core.checkFinish(key):
                return None, Constants.MENU

            printFiles(window, currentRow, games)


def printFiles(window, selected_row_idx, games):
    h, w = window.getmaxyx()

    for idx, row in enumerate(games):
        x = int(w/2 - len(row)/2)
        y = int(h / 2 - len(games) / 2 + idx)
        if idx == selected_row_idx:
            window.attron(curses.color_pair(3))
            window.addstr(y, x, " " + row + " ")
            window.attroff(curses.color_pair(3))
        else:
            window.addstr(y, x, " " + row + " ")
