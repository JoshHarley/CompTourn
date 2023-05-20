class Player:
    def __init__(self, name, villain = "", score = 0, villains_played = []):
        self.name = name
        self.villain = villain
        self.score = score    
        self.villains_played = villains_played

class Villain:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

class Setup:
    def __init__(self, villains = [], players = [], player_assigned_villains = [], villain_to_be_assigned = None):
        self.villains = villains
        self.players = players
        self.player_assigned_villains = player_assigned_villains
        self.villain_to_be_assigned = villain_to_be_assigned
