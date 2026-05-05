from src.Model.Player import Player
from typing import List
import csv


class StarcraftPlayerLoader:
    """"Charge les données de joueurs de Starcraft à partir d'un fichier CSV.
    
    On utilise les name et birthdate du fichier CSV.
    """
    def load_all_players(self) -> List[Player]:
        """Charge tous les joueurs de Starcraft à partir du fichier CSV
        et les retourne sous forme de liste d'instances de Player.
        
        Returns:
            List[Player]: liste d'instances de Player représentant les joueurs chargés.
        
        Raises:
            FileNotFoundError: si le fichier CSV n'est pas trouvable
            csv.Error: si une erreur se produit lors de la lecture du fichier
            ValueError: si les données du CSV ne sont pas au format attendu.
        """
        players_list = []
        with open('./data/starcraft_2/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row['birthdate'],
                )
                players_list.append(player)
        return players_list


if __name__ == "__main__":
    players = Starcraft2PlayerLoader().load_all_players()
    for player in players:
        print(player)