from view import Core
from view import Menu
from view import NewGame
from view import ResumeGame
from view import RunningGame
from view import Constants
from service import Storage

import curses
import sys


screen = Core.initializeFrame("BEER COUNTER")
window = Core.initializeMainWindow()
curses.doupdate()

if len(sys.argv) == 2:
    game = Storage.load(str(sys.argv[1]))
    game, key = RunningGame.init(window, game)
else:
    game = None
    key = Constants.MENU

while True:
    if key == Constants.MENU:
        key = Menu.init(window)
    elif key == Constants.NEW_GAME:
        game = NewGame.init(window)
    elif key == Constants.RESUME_GAME:
        game, key = ResumeGame.init(window)
    else:
        key = window.getch()

    if game is not None:
        game, key = RunningGame.init(window, game)

    if Core.checkFinish(key):
        break

Core.resetTerminal()

