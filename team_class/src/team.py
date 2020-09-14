class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, checked_player):
        for player in self.players:
            if player == checked_player:
                return True
        return False
    # MOST PYTHONIC VERSION OF ABOVE CODE 
    # def has_player(self, player):
    #     return self.players.count(player) > 0

    def play_game(self, result):
        if result == True:
            self.points += 3



