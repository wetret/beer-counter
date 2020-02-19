from model.Game import Game

import pickle


filetype = '.p'
folder = 'ExistingGames/'


def save(game):
    with open(folder + game.name + filetype, "wb") as filename:
        pickle.dump(game.participants, filename)


def load(filename):
    with open(folder + str(filename), "rb") as file:
        participants = pickle.load(file)

    endNameIndex = str.index(filename, filetype)
    name = filename[:endNameIndex]
    return Game(name, participants)
