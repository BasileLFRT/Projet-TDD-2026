from src.Model.Player import Player
from typing import List
import csv


class LoLPlayerLoader:
    def load_all_players(self) -> List[Player]:
        players_list = []
        with open('./data/league_of_legends/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row['birthdate'],
                )
                players_list.append(player)
        return players_list


if __name__ == "__main__":
    players = LoLPlayerLoader().load_all_players()
    for player in players:
        print(player)