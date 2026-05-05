import csv
from src.Model.Player import Player

class ChessPlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/chess/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row.get('birth_year'),
                    player_api_id=row.get('fide_id')
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = ChessPlayerLoader().load_all_players()
    for player in players:
        print(player)
