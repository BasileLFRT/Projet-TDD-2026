import csv
from src.Model.Player import Player

class CS2PlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/counter_strike_2/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row.get('birthdate'),
                    player_api_id=row.get('pseudo')
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = CS2PlayerLoader().load_all_players()
    for player in players:
        print(player)