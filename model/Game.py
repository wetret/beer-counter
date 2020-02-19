class Game:
    name = ''
    participants = []

    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def addParticipant(self, participant):
        self.participants.append(participant)