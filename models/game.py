from models.player import Player

player_list = []


class Game:
    def __init__(self, get_player_list):
        self.player_list = get_player_list

    def play(self):
        player1_wins_set = {"rock scissors", "scissors paper", "paper rock"}
        player2_wins_set = {"scissors rock", "paper scissors", "rock paper"}
        game_set = {(player_list[0].choice + " " + player_list[1].choice)}
        print(game_set)
        
        if game_set.issubset(player1_wins_set):
            return "p1"
        elif game_set.issubset(player2_wins_set):
            return "p2"
        
        return"Draw"
        
