from view import Constants

import curses


def getTitle(text):
    whiteSpaceCount = int(curses.COLS / 2 - len(text) / 2) - 1
    whiteSpace = ' '

    for i in range(0, whiteSpaceCount):
        whiteSpace += ' '

    return whiteSpace + text


def addLastLine(screen, text):
    screen.addstr(curses.LINES - 1, 0, text)


def initializeFrame(title):
    screen = curses.initscr()

    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)

    if curses.has_colors():
        curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)

    screen.keypad(True)

    title = getTitle(title)
    screen.addstr(title, curses.A_REVERSE)
    screen.chgat(-1, curses.A_REVERSE)

    addLastLine(screen, "Press 'q' to quit...")

    screen.noutrefresh()

    return screen


def initializeMainWindow():
    window = curses.newwin(curses.LINES - 3, curses.COLS - 2, 2, 1)
    window.noutrefresh()

    return window


def initLeaderWindow(window):
    leaderWindow = window.subwin(11, curses.COLS - 6, 4, 3)
    leaderWindow.bkgd(curses.color_pair(2))

    leaderWindow.noutrefresh()

    return leaderWindow


def initRankingsWindow(window):
    rankingsWindow = window.subwin(curses.LINES - 18, curses.COLS - 6, 16, 3)
    rankingsWindow.bkgd(curses.color_pair(2))

    rankingsWindow.noutrefresh()

    return rankingsWindow


def checkFinish(c):
    if c == Constants.QUIT_VIEW:
        return True
    else:
        return False


def resetTerminal():
    curses.curs_set(True)
    curses.nocbreak()
    curses.echo()

    curses.endwin()
