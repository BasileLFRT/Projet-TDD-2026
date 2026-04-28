from src.Common.utils import print_timings
from src.Model.Player import Player
from typing import List
import csv

# Note for students:
# All "PlayerLoader" classes, even maybe all "Loader" classes, will look the same,
# you may be able to use inheritance to your advantage

class FootballPlayerLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    @print_timings
    def load_all_players(self) -> List[Player]:
        players_list = []
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Note:
                # The specifics of
                player = Player(row['player_api_id'], row['player_name'])
                players_list.append(player)

        return players_list
