from view import Core
from view import Constants
from service import Storage
from service import Input
from service import Sound

import curses
import pyfiglet


def init(window, game):
    window.bkgd(curses.color_pair(3))
    window.clear()
    window.box()
    window.keypad(True)

    window.addstr(0, 2, "RUNNING GAME: " + game.name)
    window.refresh()

    leaderWindow = Core.initLeaderWindow(window)
    leaderWindow.box()
    leaderWindow.addstr(0, 2, "LEADER")
    leaderWindow.refresh()

    rankingsWindow = Core.initRankingsWindow(window)
    rankingsWindow.box()
    rankingsWindow.addstr(0, 2, "RANKINGS")

    participants = game.participants
    sortedParticipants = sort(participants.copy())

    leader = sortedParticipants[0]

    drawLeader(leaderWindow, leader)
    drawRankings(rankingsWindow, participants)

    Input.init()
    isDecrease = False

    while True:
        # this is used for testing
        # key = window.getch()
        # if key != Constants.QUIT_VIEW:
        #     key = Input.getInput(len(participants))

        pressedButtons = Input.getInput()
        key = pressedButtons[0]

        if Core.checkFinish(key):
            Storage.save(game)
            return None, Constants.MENU
        else:
            if len(participants) > key and not isDecrease:
                Sound.playNewBeerOpen()
                participants[key].increase()
            else:
                if isDecrease and len(participants) > key:
                    Sound.playBooh()
                    participants[key].decrease()
                    isDecrease = False
                else:
                    isDecrease = True

            sortedParticipants = sort(participants.copy())

        if sortedParticipants[0] != leader:
            leader = sortedParticipants[0]
            Sound.playNewLeader()

        drawLeader(leaderWindow, leader)
        drawRankings(rankingsWindow, participants)
        Storage.save(game)


def sort(participants):
    return sorted(participants, key=lambda x: x.count, reverse=True)


def drawLeader(window, leader):
    asciiArtCount = pyfiglet.Figlet(font="banner3", width=100).renderText(str(leader.count))
    asciiArtName = pyfiglet.Figlet(font="banner3", width=100).renderText(str(leader.name, "utf-8"))

    nameLines = asciiArtName.split("\n")
    countLines = asciiArtCount.split("\n")

    h, w = window.getmaxyx()

    for i in range(0, len(countLines)):
        window.addstr(i + 2, 4, " " * (int(w)-5))
        window.addstr(i + 2, 4, countLines[i])
        window.addstr(i + 2, 28, nameLines[i])

    window.refresh()


def drawRankings(window, participants):
    h, w = window.getmaxyx()

    for i in range(0, 2*len(participants), 2):
        window.addstr(i + 2, 4, " " * (int(w)-5))
        window.addstr(i + 2, 4, participants[int(i/2)].name)

        window.addstr(i + 2, 15, '|')
        for j in range(0, participants[int(i/2)].count):
            window.addstr(i + 2, j * 4 + 16, '█|█|')
        window.addstr(i + 2, participants[int(i/2)].count * 4 + 20, str(participants[int(i/2)].count))

    window.refresh()
