import csv
from src.Model.Player import Player

class VolleyballMenPlayerLoader:
    """Charge les données des joueurs de volley masculin à partir d'un fichier CSV.
    
    Utilise les colonnes name et birth_date du CSV pour créer des instances de Player.
    """
    def load_all_players(self) -> list[Player]:
        """Transforme les données du CSV en une liste d'instances de Player.
        
        Returns:
            list[Player]: une liste d'instances de Player créées à partir des données du CSV.
        
        Raises:
            FileNotFoundError: si le fichier CSV n'est pas trouvable.
            KeyError: si des colonnes sont manquantes.
        """
        players_list = []
        with open('./data/volleyball/player_men.csv', newline='') as csvfile:
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
    players = VolleyballMenPlayerLoader().load_all_players()
    for player in players:
        print(player)