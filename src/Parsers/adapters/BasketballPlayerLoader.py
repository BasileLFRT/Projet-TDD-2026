import csv
from src.Model.Player import Player

class BasketballPlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/basketball/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=f"{row['first_name']} {row['last_name']}",
                    birthdate=None,
                    player_api_id=row.get("person_id")
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = BasketballPlayerLoader().load_all_players()
    for player in players:
        print(player)