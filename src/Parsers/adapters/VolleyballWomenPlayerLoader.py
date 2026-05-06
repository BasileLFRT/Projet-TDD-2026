import csv
from src.Model.Player import Player

class VolleyballWomenPlayerLoader:
    """Charge les données des joueuses de volleyball à partir d'un fichier CSV et les convertit en objets Player.
    
    Utilise les colonnes 'name' et 'birth_date' du fichier CSV pour créer les instances de Player."""
    def load_all_players(self) -> list[Player]:
        """Transforme les données des joueuses de volleyball en une liste d'instances de Player.
        
        Returns:
            list[Player]: Une liste d'instances de Player représentant les joueuses de volleyball.
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes 'name' ou 'birth_date' sont manquantes dans le fichier CSV.
        """
        players_list = []
        with open('./data/volleyball/player_women.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row.get('birth_date'),
                    player_api_id=None
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = VolleyballWomenPlayerLoader().load_all_players()
    for player in players:
        print(player)