import csv
from src.Model.Player import Player

class ChessPlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/chess/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_name = row['name']
                if ',' in raw_name:
                    parts = raw_name.split(',', 1)
                    nom = f"{parts[1].strip()} {parts[0].strip()}"
                else:
                    nom = raw_name
                player = Player(
                    nom=nom,
                    birthdate=row.get('birth_year'),
                    player_api_id=row.get('fide_id')
                )
                players_list.append(player)
        return players_list