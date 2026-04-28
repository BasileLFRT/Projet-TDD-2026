from src.Common.utils import print_timings
from src.Model.Player import Player
from typing import List
import csv

# Note for students:
# All "PlayerLoader" classes, even maybe all "Loader" classes, will look the same,
# you may be able to use inheritance to your advantage

class FootballPlayerLoader:
    def load_all_players(self) -> List[Player]:
        players_list = []
        with open('./data/football_european_leagues/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(nom=row['player_name'], birthdate=None)
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = FootballPlayerLoader().load_all_players()
    for player in players:
        print(player)