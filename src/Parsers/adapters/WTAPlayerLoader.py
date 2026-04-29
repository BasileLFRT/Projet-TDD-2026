import csv
from src.Model.Player import Player

class WTAPlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/tennis/wta_players_2024.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=f"{row['name_first']} {row['name_last']}",
                    birthdate=None,
                    player_api_id=row.get("player_id")
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = WTAPlayerLoader().load_all_players()
    for player in players:
        print(player)