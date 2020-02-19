import os
from threading import Thread


def playNewBeerOpen():
    thread = Thread(target=play, args=('Sounds/beer-open.mp3', ))
    thread.start()


def playBooh():
    thread = Thread(target=play, args=('Sounds/booh.mp3', ))
    thread.start()


def playNewLeader():
    thread = Thread(target=play, args=('Sounds/new-leader.mp3', ))
    thread.start()


def play(songPath):
    os.system('mpg123 -q ' + songPath + ' &>/dev/null')
