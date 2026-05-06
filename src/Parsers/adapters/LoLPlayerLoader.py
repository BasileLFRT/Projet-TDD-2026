from src.Model.Player import Player
from typing import List
import csv


class LoLPlayerLoader:
    """Charge les données des joeurs de LOL à partir d'un CSV
    
    utilise les colonnes name et birthdate du CSV pour créer des instances de Player"""
    def load_all_players(self) -> List[Player]:
        """ Transforme les données du CSV en une liste d'instances de Player 
        
        Returns:
            List[Player]: une liste d'instances de Player créées à partir des données du
        
        Raises:
            FileNotFoundError: si le fichier CSV n'est pas trouvé
            KeyError: si des colonnes sont manquantes
        """
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
