class Elevator:
    def __init__(self, current_floor):
        self.make = "Elevator Company"
        self.model = "Elevator Model"
        self.floor = current_floor

elevator = Elevator(1)
print(elevator.make)
print(elevator.model)
print(elevator.floor)

class Participant:
    def _init_(self):
        self.points = 0
        self.choice = ""

class GameRound:
    def _init_(self):
        self.participants = []
        self.round_number = 0
        self.round_winner = ""

class Game:
    def _init_(self):
        self.endgame = False
        self.participant = Participant()
        self.secondParticipant = Participant()

#https://github.com/MicrosoftDocs/mslearn-python-oo
