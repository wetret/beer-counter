from model.Person import Person
from model.Game import Game

import curses


def init(window):
    window.bkgd(curses.color_pair(2))
    window.clear()
    window.box()
    window.keypad(False)

    window.addstr(0, 2, "NEW GAME")

    curses.echo()

    window.addstr(1, 4, "Enter the name of the game:   ")
    gameName = ''

    while len(gameName) == 0:
        gameName = window.getstr(1, 32)

        if len(gameName) == 0:
            window.addstr(1, 60, "The game name cannot be empty")
        else:
            window.addstr(1, 60, "                             ")

    participantsCount = 0
    participants = []

    while participantsCount < 2:
        window.addstr(2, 4, "Enter the number of participants:   ")

        participantsCount = int(window.getstr(2, 38))

        if participantsCount < 2:
            window.addstr(2, 60, "More then 1 participant needed")
        else:
            window.addstr(2, 60, "                              ")

    i = 0
    while i < participantsCount:
        window.addstr(i + 3, 4, "Enter the name of participant " + str(i + 1) + ": ")
        participantName = window.getstr(i + 3, 38)

        if len(participantName) == 0:
            window.addstr(i + 3, 60, "The name cannot be empty")
        else:
            window.addstr(i + 3, 60, "                        ")
            participants.append(Person(participantName))
            i += 1

    game = Game(str(gameName, "utf-8"), participants)

    curses.noecho()
    return game
