from src.Common.utils import print_timings
from src.Model.Player import Player
from typing import List
import csv

# Note for students:
# All "PlayerLoader" classes, even maybe all "Loader" classes, will look the same,
# you may be able to use inheritance to your advantage

class FootballPlayerLoader:
    """Charge les joueurs de football depuis player.csv issu du Football européen
    avec les colonnes player_name et birthdate
    """
    def load_all_players(self) -> List[Player]:
        """Lit le fichier CSV et retourne la liste de tous les joueurs.
        
        Chaque ligne est convertie en instance de Player.

        Returns:
            List[Player]: Liste des joueurs chargés, vide si le fichier l'est
            
        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable
            KeyError: Si une colonne obligatoire est absente du CSV."""
        players_list = []
        with open('./data/football_european_leagues/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(nom=row['player_name'], birthdate=None)
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = FootballPlayerLoader().load_all_players()
    for player in players:
        print(player)