# src/Parsers/adapters/BadmintonPlayerLoader.py
import csv
from src.Model.Player import Player

class BadmintonPlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/badminton/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=None,
                    player_api_id=None
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = BadmintonPlayerLoader().load_all_players()
    for player in players:
        print(player)