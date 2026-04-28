import csv
from src.Model.Player import Player

class ChampionsLeaguePlayerLoader:
    def load_all_players(self) -> list[Player]:
        players_list = []
        with open('./data/football_champions_league/player.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                player = Player(
                    nom=row["player_name"],
                    birthdate=None,
                    player_api_id=None
                )
                players_list.append(player)
        return players_list