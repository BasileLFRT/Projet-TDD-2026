# src/Parsers/adapters/BadmintonPlayerLoader.py
import csv
from src.Model.Player import Player

class BadmintonPlayerLoader:
    """Classe permettant de charger les données des joueurs de badminton à partir d'un fichier CSV.

    Lit les données du fichier 'player.csv' lié au badminton et en crée des instances de Player
    """
    def load_all_players(self) -> list[Player]:
        """ Lit le fichier CSV de badminton et en liste les joueurs

        Returns:
            list[Player]: Une liste d'instances Player qui sont les joueurs chargés

        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé
        """
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